from multiprocessing import context
from typing import Union
from urllib import request
import calendar
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./src/templates")


@app.get("/")
def home(request: Request):
    """
    Displays the app dashboard
    """
    return  templates.TemplateResponse("home.html", {
        "request" : request
    })

@app.post("/stock")
def create_stock():

    """
    Creates a Stock in the database
    """
    return {
        "code" : "Success",
        "message" : "Created"
    }