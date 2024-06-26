import uvicorn
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

'''
路径参数：路径中存在形参，视图函数对应形参
查询参数：路径中没写明形参则默认为查询参数
'''

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # 声明查询参数
    return fake_items_db[skip: skip + limit]

if __name__ == '__main__':
    uvicorn.run("查询参数:app", host='127.0.0.1', port=8000, reload=True)