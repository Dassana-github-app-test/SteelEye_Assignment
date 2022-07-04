from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models
import datetime as dt
app = FastAPI()


class TradeDetails(BaseModel):
    buySellIndicator:str
    price:float
    quantity:int
class Trade(BaseModel):
    asset_class:Optional[str]
    counterparty:Optional[str]
    instrument_id:str
    instrument_name:str
    trade_date_time: dt.datetime
    trade_details:TradeDetails
    trade_id:str
    trader:str

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get('/trade_list', response_model=List[Trade], status_code=200)
def get_all_items():
    items = db.query(models.Trade).all()
    return items


@app.get('/single_trade/{trade_id}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(trade_id: int):
    item = db.query(models.Trade).filter(models.Trade.trade_id == trade_id).first()
    return item
@app.get('/get_counter_party/{counter_party_id}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(counter_party_id: int):
    item = db.query(models.Trade).filter(models.Trade.counterparty == counter_party_id).first()
    return item
@app.get('/instrument_id/{instrumentId}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(instrumentId: int):
    item = db.query(models.Trade).filter(models.Trade.instrument_id == instrumentId).first()
    return item
@app.get('/instrument_Name/{instrumentName}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(instrumentName: int):
    item = db.query(models.Trade).filter(models.Trade.instrument_name == instrumentName).first()
    return item
@app.get('/asset_class/{asset_class}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(asset_class: str):
    item = db.query(models.Trade).filter(models.Trade.asset_class == asset_class).first()
    return item
@app.get('/maxPrice/{maxPrice}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(maxPrice: int):
    item = db.query(models.Trade).filter(models.TradeDetails.price == maxPrice).first()
    return item
@app.get('/trader/{trader_name}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(minPrice: int):
    item = db.query(models.Trade).filter(models.TradeDetails.price == minPrice).first()
    return item
@app.get('/trade_type/{trade_type}', response_model=Trade,status_code=status.HTTP_200_OK)
def get_an_item(trade_type: int):
    item = db.query(models.Trade).filter(models.Trade.trade_details == trade_type).first()
    return item