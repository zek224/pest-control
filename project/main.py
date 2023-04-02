# main.py
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader, select_autoescape

app = FastAPI()
current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount('/static', StaticFiles(directory=os.path.join(current_dir, 'static')), name='static')

env = Environment(
    loader=PackageLoader("project"),
    autoescape=select_autoescape()
)
#templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
#root route
async def home():
    #get and load the home template
    homeTemplate = env.get_template("home.html")
    return homeTemplate.render()
    #return home.render()
    #return templates.TemplateResponse("home.html", {"request": request})
    #return {"greeting":"Hello world"}

@app.get("/about", response_class=HTMLResponse)
async def about():
    #get and load the about page
    aboutTemplate = env.get_template("about.html")
    return aboutTemplate.render()

@app.get("/signin", response_class=HTMLResponse)
async def signin():
    #get and load the about page
    aboutTemplate = env.get_template("signin.html")
    return aboutTemplate.render()

@app.get("/dataEntry", response_class=HTMLResponse)
async def dataEntry():
    #get and load the dataEntry page
    dataEntryTemplate = env.get_template("dataEntry.html")
    return dataEntryTemplate.render()
    

@app.get("/visualizations", response_class=HTMLResponse)
async def visualizations():
    #get and load the visualizations page
    visualizationsTemplate = env.get_template("visualizations.html")
    return visualizationsTemplate.render()

@app.post("/sendEntry")
async def sendEntry():
    source_id = Request.json['source_id']
    measurement = Request.json['measurement']
    farm_id = Request.json['farm_id']
    date = Request.json['date']