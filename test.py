
# 基础写法
def get_full_name(first_name, last_name):
    pass

# 声明参数类型  title() 首字母大写
def get_full_name(first_name:str, last_name:str):
    return first_name.title() + "" + last_name.title()


# 声明容器参数类型及其子类类型
from typing import List
def get_full_name2(first_name: List[str]):
    pass

# Dict[str, float] k:str v:float
from typing import Dict
def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# Pydantic 模型¶

from pydantic import ValidationError
from datetime import datetime
from pydantic import BaseModel, PositiveInt
from typing import Optional


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    # signup_ts: datetime | None   # 参数必须传 值可以是空
    signup_ts: Optional[datetime] = None  # 默认值为空  参数可不传
    tastes: dict[str, PositiveInt]
data = {
    'id':123,
    'name':"123",
    # "signup_ts":None,
    'tastes':{"11":11},
}
# u = User(**data)

from typing import Tuple

def process_data(data: Tuple[int, str]) -> str:
    return f"ID: {data[0]}, Name: {data[1]}"


from typing import List, Tuple, Set, Dict

def process_items(items: List[int]) -> Tuple[int, int]:
    return min(items), max(items),items


# print(process_items(1))

import requests

headers = {
  'Accept': 'text/html, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Connection': 'keep-alive',
  'Cookie': 'dxm_i=MTYxMTI2NyFhVDB4TmpFeE1qWTMhZWRmNGM0ZTA5NDY5ZTg0NWUyZWQ0ZjQ2OWNhZjcyOGM; dxm_t=MTcxODc4Mjk5OCFkRDB4TnpFNE56Z3lPVGs0ITZlNzg1ZmRhZDA1M2QzNzcyMTMzOTIwYTAxZmJlYjMw; dxm_c=YjF2QXVKZ3chWXoxaU1YWkJkVXBuZHchNWYxZjMzNmRkMjBkMzRkNDcxODM3YzllM2JjNTA0Njg; dxm_w=NzgyODg2YTY1ZTIwMGRjMDkzYjNlMjYzMTcwZDFjYjQhZHowM09ESTRPRFpoTmpWbE1qQXdaR013T1ROaU0yVXlOak14TnpCa01XTmlOQSE2MmE3MjEwYTNiNmU1MzBjZmExY2QzOTdhYzEyMmQxZg; dxm_s=hx4VjA9cFbkHBz0sHzLuloiHQV6CdW9-SzvNsiLAr8s; _dxm_ad_client_id=CD59750D7F6687AF6D1022FE8AA2F8236; JSESSIONID=A89E5FD388623CB9886E8151024A2221; JSESSIONID=9A265DAE17DDAB8C0DC477A365A03EE7',
  'Referer': 'https://www.dianxiaomi.com/order/index.htm',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

url = 'https://www.dianxiaomi.com/printMb.htm?authId=95607896162538733&packageIds=95607909315493249&orderField=sku&isDesc=0&isCos=1'
res = requests.get(url,headers=headers,allow_redirects=True)
print(res.status_code)
f = open('qqq.pdf','wb')
f.write(res.content)
f.close()
