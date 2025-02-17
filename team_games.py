
import requests

def get_team_games(team_id : int):
    url = f"https://api.balldontlie.io/v1/games?team_ids[]={team_id}&per_page=100"
    api_key = "fbb2b6b3-2335-48ec-8383-635cb99666ee"
    headers = {"Authorization": f"{api_key}"}

    response = requests.get(url , headers=headers)

    if response.status_code == 200:
        team_game = response.json()
        return team_game
    return None
