import random

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

class player():

  def __init__(self,playername,money,firepower,openingwin,openingrate,riflerating,pistolrating,ecorating,hs,awp,awprating,supportrating,iglrating):
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
    self.supportrarting = supportrating # probably not going to be used
    self.iglrating = iglrating # probably not going to be used

class game():

  def __init__(self,team1,team2):
    self.team1 = team1
    self.team2 = team2

  def fast(self): # calculates each round
    rounds = 1 
    half = 0 # first 15 rounds
    
    while half < 2: # Regulation
      # Pistol Round
      print("Round 1")
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

####
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