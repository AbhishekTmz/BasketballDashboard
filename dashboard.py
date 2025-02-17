from team_games import get_team_games
from get_all_team import get_all_team


# Function to get team ID based on team name
def get_team_id (team_name:str):
    teams = get_all_team()
    for team in teams.get("data",[]): # Iterate through the team list
        if team["full_name"].lower() == team_name.lower():
            return team["id"] # Return team ID if found
    return None

# Function to calculate team performance metrics
def dashboard(team_name:str):
    team_id = get_team_id(team_name)
    if team_id is None:
        return {"error": "Team not found"} # Return error if team does not exist
    
    team_games = get_team_games(team_id)
    if team_games is None:
        return {"error": "Failed to get team games"}
    
    total_games_played = len(team_games["data"])
    print(total_games_played)  # Debugging: Print total games played
     # Calculate win percentage (avoid division by zero)
    wins = sum(1 for game in team_games["data"] if 
               (game["home_team"]["id"] == team_id and game["home_team_score"] > game["visitor_team_score"]) or 
               (game["visitor_team"]["id"] == team_id and game["visitor_team_score"] > game["home_team_score"]))
    losses = total_games_played - wins

    win_percent = (wins/total_games_played) * 100 if total_games_played > 0 else 0 
       # Return dictionary with team performance stats
    return {
        "team_name": team_name,
        "team_id": team_id,
        "total_games_played": total_games_played,
        "wins": wins,
        "losses": losses,
        "win_percent": round(win_percent , 2)
    }



    