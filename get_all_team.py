import requests

def get_all_team():
    url ="https://api.balldontlie.io/v1/teams"
    api_key = "fbb2b6b3-2335-48ec-8383-635cb99666ee"
    headers = {"Authorization": f"{api_key}"}

    response = requests.get(url , headers=headers)
    
    if response.status_code == 200:
        all_team =response.json()
        return all_team
    return None


    
