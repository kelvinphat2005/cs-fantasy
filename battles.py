import random
from players.playerio import readplayer
from teams.teamio import readteam

# CS rounds are 155s

money = [800,800,800,800,800,800,800,800,800,800]
# {PRICE: FIREPOWER}
pistol = {0: 1, 300: 2, 700: 5}
# USP-S, P250, DEAGLE
eco = {1100: 6, 1700: 6}
# MP-9/MAC-10, SSG-08
full_ct = {2050: 8, 2900: 10, 3100: 11, 4750: 16}
# FAMAS, M4A1-S, AUG, AWP
full_t = {1800: 8, 2700: 11, 4750: 16}
# GALIL, AK-47, AWP
util = {650: 1, 1000: 2, 500: 1, 300: 1, 200: 1, 300: 1}
# KEVLAR, KEVLAR + HELMET, MOLLY, SMOKE, FLASH, HE

'''
Game Simulation
'''

# Add Player
class player():

  def __init__(self,playername,money,firepower,openingwin,openingrate,riflerating,pistolrating,ecorating,hs,awp,awprating):
    self.playername = playername
    self.money = money
    self.firepower = firepower
    self.openingwin = openingwin
    self.openingrate = openingrate
    self.riflerating = riflerating
    self.pistolrating = pistolrating
    self.ecorating = ecorating
    self.hs = hs
    self.awp = awp
    self.awprating = awprating
    return

  def money(self,change): # add or remove money
    self.money += change
    return

  def firepower(self,change): # add or remove firepeower
    self.firepower += change
    return

# Creating Players
def load_player(team,playernum):
  team_info = readteam(team)
  player_info = readplayer(team_info[playernum])
  player1 = player(player_info[0],800,0,player_info[1],player_info[2],player_info[3],player_info[4],player_info[5],player_info[6],player_info[7],player_info[8])
  return player1

# Game
class game():

  def __init__(self,team1,team2):
    self.team1 = team1
    self.team2 = team2

  def fast(self): # calculates each round
    # Loading player
    print("LOADING PLAYERS")
    player1 = load_player(self.team1,1)
    player2 = load_player(self.team1,2)
    player3 = load_player(self.team1,3)
    player4 = load_player(self.team1,4)
    player5 = load_player(self.team1,5)
    player6 = load_player(self.team2,1)
    player7 = load_player(self.team2,2)
    player8 = load_player(self.team2,3)
    player9 = load_player(self.team2,4)
    player10 = load_player(self.team2,5)

    print(player10.money)
    print(player10.awp)

    rounds = 1 
    half = 0 # first 15 rounds
    
    while half < 2: # Regulation
      # Pistol Round
      print("Round " + str(rounds))
      while rounds < 14: # Half
        
        rounds += 1
        break
      half += 1

    # OT
    return

  def advanced(self): # calculates each second
    secs = 0
    while secs < 155:
      break

team1 = readteam("test")
team2 = readteam("test 2")
run = game("test", "test 2")
run.fast()

'''
def bo1(self,odds1):
    print("Best of 1: ")
    global ot_number
    ot_number = 1
    team1 = 0 # team 1 rounds
    team2 = 0 # team 2 rounds
    print(self.odds1)
    while team1 <= (ot_number*3)+12 and team2 <= (ot_number*3) + 12:
      odds = random.randint(0,100)
      # check for overtime
      if team1 >= (ot_number*3) + 12 and team2 >= (ot_number*3) + 12:
        score = overtime(ot_number,team1,team2,odds1)
        team1 = score[0]
        team2 = score[1]
        ot_number = score[2]
      # add score if not overtime
      else: 
        if odds < self.odds1: # regulation rounds
          team1 += 1
        else:
          team2 += 1
    print(str(team1) + " - " + str(team2))
    if team1 > team2:
      return 1
    else:
      return 2
'''