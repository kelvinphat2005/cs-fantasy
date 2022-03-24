from players import Players
from teams import Teams

def main():
  print("Hello World")
  test("team1","team2")
  return

def test(team1: str,team2: str):
  # Initialize Players
  print("Initializing Players")
  team1 = get_players("team1") #very efficient code
  team2 = get_players("team2")
  team1 = get_stats(team1)
  team2 = get_stats(team2)
  # print(f"Team 1 Players: {team1}")
  # print(f"Team 2 Players: {team2}")
  
'''

Grabbing Stats

'''

# Get players (Names) from the team and return a list of players
def get_players(team_name: str):
  players_in_team = []
  
  # load all teams 
  Teams.all.clear()
  Teams.instantiate_from_csv()

  # going through all the teams
  count = 0
  for current_team in Teams.all:
    if current_team.name == team_name:
      players_in_team.append(current_team.player1)
      players_in_team.append(current_team.player2)
      players_in_team.append(current_team.player3)
      players_in_team.append(current_team.player4)
      players_in_team.append(current_team.player5)
      break # FOUND
    count += 1
  # print(players_in_team)
  return players_in_team

# Create list of player stats from a list of players
def get_stats(player_list: list):
  player_stats = []

  # load all players
  Players.all.clear()
  Players.instantiate_from_csv()
  
  # look for players
  for player in Players.all:
    if player.name in player_list:
      print(f"Name: {player.name} Info: {player}")
      player_stats.append(player)
  
  return player_stats

'''

main

'''
if __name__ == "__main__":
  main()