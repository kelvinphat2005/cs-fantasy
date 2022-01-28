from players.playerio import *

def readteam(team):
  value = []
  file = open("teams/" + team + ".txt","r")
  value = file.readlines()

  # removings /n
  count = 0
  for i in value:
    value[count] = i.strip()
    count += 1

  file.close()
  return value

def writeteam(team,input_list):
  file = open("teams/" + team + ".txt", "w")
  for i in input_list:
    file.write(i + "\n")
  file.close()
  return

# lines 1-6 reserved for players & coach
def addplayer(team,player_num,player_name):
  team_info = readteam(team)
  team_info[player_num] = player_name
  writeteam(team,team_info)
  return

def modify(team):
  team_info = readteam(team)
  # show team info
  print("Team Name: " + team_info[0])
  i = 1
  while i <= 6: # Show Players
    print("Player " + str(i) + ": " + team_info[i])
    i += 1

  # Menu
  x = input("[1] Change Players [2] Exit --> ")
  return

# calculate new team stats based on player stats
def calculate(team):
  team_info = readteam(team)
  # creating list of player in team
  player_list = []
  i = 1
  while i <= 6:
    player_list.append(team_info[i])
    i += 1
  # getting player stats
  i = 0
  while i <= 5:
    readplayer(player_list[i])

  openingwin = 0
  openingrate = 0
  # Overall
  riflerating = 0
  pistolrating = 0
  ecorating = 0
  # AWP
  awp = 0
  awprating = 0
  # Support
  supportrating = 0
  stratrating = 0
  return

def teamio_menu():
  return
