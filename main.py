from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.database.Model import Model
from app.modules.opgg import *
db = Model()
app = FastAPI()


origins = [
    'http://streamer-network.netlify.app/',
    'https://streamer-network.netlify.app/',
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:3002',
    'http://localhost:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

dummy_data = {
    'node': [
        {'id': '마리마리착마리', 'value': 1},
        {'id': '루모그래프', 'value': 1},
        {'id': '꿀벌지민', 'value': 1},
        {'id': '리듬타지마', 'value': 1}
    ],
    'edge': [
        {'from': '마리마리착마리', 'to': '루모그래프', 'value': 10},
        {'from': '마리마리착마리', 'to': '꿀벌지민', 'value': 5},
        {'from': '루모그래프', 'to': '꿀벌지민', 'value': 15},
        {'from': '루모그래프', 'to': '리듬타지마', 'value': 3},
        {'from': '꿀벌지민', 'to': '리듬타지마', 'value': 1}
    ]
}

@app.get("/")
def read_root():
  return dummy_data

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    user_log = getUserAllGameData('침대에서 뒹굴')
    print(user_log[0])
    db.insertUserLog(user_log)
    
