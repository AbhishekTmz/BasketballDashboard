from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates
import requests
import uvicorn
from team_player import get_team_players
from get_all_team import get_all_team
from dashboard import dashboard , get_team_id


app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Route for home page displaying all NBA teams
@app.get("/")
def home(request : Request):
    teams = get_all_team()
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "teams": teams.get("data" , [])
        })

# Route for team dashboard displaying performance and players
@app.get("/dashboard/{team_name}")
def dashboard_screen(request : Request , team_name = str):
    teams = get_all_team()
    performance = dashboard(team_name)

    team_id = get_team_id(team_name)
    players= get_team_players(team_id)if team_id else []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "teams":teams.get("data", []),
        "performance": performance ,
        "players": players
    })

uvicorn.run(app,host='0.0.0.0', port=8000)




