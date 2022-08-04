from typing_extensions import final
from pydantic import BaseModel
from models import models
from routers import stocks
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from services.SQLiteConnector import SessionLocal, engine
from sqlalchemy.orm import Session

tags_metadata = [
    {
        'name': 'stocks',
        'description': 'Operations with stocks.'
    }
]


app = FastAPI(openapi_tags=tags_metadata)

# models.Base.metadata.create_all(bind=engine)


templates = Jinja2Templates(directory="./templates")

@app.get("/")
def home(request: Request):
    """
    Displays the app dashboard
    """
    return  templates.TemplateResponse("home.html", {
        "request" : request
    })

app.include_router(stocks.router)