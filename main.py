from players import Players
from teams import Teams

# List of Players
team1 = []
team2 = []

teams = [team1,team2]

def main():
  print("Hello World")
  print(calculate_odds())
  return

# Calculate odds of team1 winning: returns range(0,1)
def calculate_odds():
  odds = 0
  # 0 = Eco/Pistol
  # 1 = Half Buy (2-3 Rifles)
  # 2 = Full Buy (At least 4 rifles)
  # [team1_round_type, team2_round_type]
  round_type = [0,0]
  team1, team2 = load_players("team1","team2")
  # [team1_firepower, team2_firepower]
  firepower = [0,0]

  print(team1)
  print(team2)
  teams = [team1,team2]
  
  # identify team buy
  for x in range(2):
    rifle_count = 0
    print(teams[x])
    for i in teams[x]: # check through team for rifles
      if i.gun == "rifle":
        rifle_count += 1
        print("Rifle")
      else:
        print("No Rifle")
    if rifle_count > 4:
      print(f'Team {x+1}: Rifle Round')
      round_type[x] = 2
    elif rifle_count > 2:
      print(f'Team {x+1}: Half Buy')
      round_type[x] = 1
    else:
      print(f'Team {x+1}: Eco/Pistol Round')
      round_type[x] = 0

      
  return odds

def load_players(team_a,team_b):
  print("Initializing Players")
  team1 = get_players(team_a) #very efficient code
  team2 = get_players(team_b)
  team1 = get_stats(team1)
  team2 = get_stats(team2)
  return team1, team2
  
# check if working correctly
def test(team1: str,team2: str):
  # Initialize Players
  print("Initializing Players")
  team1test = get_players("team1") #very efficient code
  team2test = get_players("team2")
  team1test = get_stats(team1test)
  team2test = get_stats(team2test)
  print("Printing out objects in team1")
  for i in team1test:
    print(i)

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
      # print(f"Name: {player.name} Info: {player}")
      player_stats.append(player)
  
  return player_stats

'''

main

'''
if __name__ == "__main__":
  main()