# main.py
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount('/static', StaticFiles(directory=os.path.join(current_dir, 'static')), name='static')

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return {"greeting":"Hello world"}
    