from fastapi import APIRouter, Request, Depends, BackgroundTasks
from requests import Session
from models.models import Stock
from services.SQLiteConnector import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import models

router = APIRouter(prefix="/stock", tags=['stocks'])

class StockRequest(BaseModel):
    ticker: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.id == id).first()

    db.add(stock)
    db.commit()

@router.post("/")
async def create_stock(stock_request: StockRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Creates a Stock in the database
    """

    stock = models.Stock()

    stock.ticker = stock_request.ticker

    db.add(stock)
    db.commit()
     
    background_tasks.add_task(fetch_stock_data, stock.id)

    return {
        "code" : "Success",
        "message" : "Created"
    }

@router.get('/')
async def get_stock_info(ticker: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Get Stock Information
    """
    stock = models.Stock()

    stock.ticker = ticker
    
    background_tasks.add_task(fetch_stock_data, stock.id)

    return "OK"