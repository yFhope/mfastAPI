from fastapi import FastAPI

app = FastAPI()

'''
路径参数：路径中存在形参，视图函数对应形参
查询参数：路径中没写明形参则默认为查询参数
'''
# 基础写法
@app.get("/items/{item_id}")  # 路由
async def read_item(item_id):  # 函数参数
    return {"item_id": item_id}


# 限制参数类型的
@app.get("/items2/{item_id}")
async def read_item2(item_id: int):
    return {"item_id": item_id}

# 参数限制 + pydantic数据校验 + Enum枚举 限制范围  TODO 预定义路径参数
from enum import Enum
class ModelName(str, Enum):   # Enum限制参数范围只能是这三个  TODO 预定义路径参数
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}