from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

app = FastAPI()


class FormData(BaseModel):
    username: str
    pwd: str
    ecm: list
    fid: int

    @validator('ecm', pre=True)
    def check_ecm(cls, v):
        if not isinstance(v, list):
            raise ValueError("ECM must be a list")
        return v

    @validator('fid', pre=True)
    def check_fid(cls, v):
        if not isinstance(v, int):
            raise ValueError("FID must be an integer")
        return v


# 假设我们用一个简单的字典来模拟数据库存储
data_store = {}


@app.post("/submit/")
async def submit_data(form_data: FormData):
    print("校验通过的数据：",form_data)
    # 使用username作为键，因为用户名应该是唯一的
    if form_data.username in data_store:
        raise HTTPException(status_code=409, detail="Username already exists")
    data_store[form_data.username] = form_data.dict()
    return {"message": "Data submitted successfully"}


@app.get("/read/{username}")
async def read_data(username: str):
    user_data = data_store.get(username)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data


@app.put("/update/{username}")
async def update_data(username: str, updated_data: FormData):
    if username not in data_store:
        raise HTTPException(status_code=404, detail="User not found")
    data_store[username] = updated_data.dict()
    return {"message": "Data updated successfully"}


@app.delete("/delete/{username}")
async def delete_data(username: str):
    if username not in data_store:
        raise HTTPException(status_code=404, detail="User not found")
    del data_store[username]
    return {"message": "Data deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)