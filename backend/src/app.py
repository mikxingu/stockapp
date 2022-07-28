from typing_extensions import final
from pydantic import BaseModel
from models import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from services.SQLiteConnector import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="./templates")

class StockRequest(BaseModel):
    ticker: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request):
    """
    Displays the app dashboard
    """
    return  templates.TemplateResponse("home.html", {
        "request" : request
    })

@app.post("/stock")
def create_stock(stock_request: StockRequest, db: Session = Depends(get_db)):

    """
    Creates a Stock in the database
    """

    stock = models.Stock()

    stock.ticker = stock_request.ticker


    db.add(stock)
    db.commit()
     
    return {
        "code" : "Success",
        "message" : "Created"
    }