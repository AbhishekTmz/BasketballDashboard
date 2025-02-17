
import requests

def get_team_players(team_id : int):
    url = f"https://api.balldontlie.io/v1/players?team_ids[]={team_id}"
    api_key = "fbb2b6b3-2335-48ec-8383-635cb99666ee"
    headers = {"Authorization": f"{api_key}"}

    response = requests.get(url , headers=headers)

    if response.status_code == 200:
        players_data = response.json()
        print(players_data)

        return players_data.get("data", [])
    return []  
