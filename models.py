from database import Base
from typing import Optional
import datetime as dt
from sqlalchemy import String,Float,Integer,Column,Boolean,DateTime
from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text

class TradeDetails(Base):
    __tablename__= 'tradeDetails'
    buySellIndicator=Column(String)
    price:Column(Float)
    quantity:Column(Float)
class Trade(Base):
    __tablename__='trades'
    __table_args__ = {'extend_existing': True}
    asset_class=Column(String)
    counterparty: Column(String)
    instrument_id: Column(String, unique=True)
    instrument_name: Column(String)
    trade_date_time: Column(DateTime)
    trade_details = Column(TradeDetails)
    trade_id = Column(String, primary_key=True)
    trader: Column(String)
    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"