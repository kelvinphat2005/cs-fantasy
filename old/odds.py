import random

ot_number = 1

def edit_odds():
  print("Round winrate %")
  odds = int(input("Round win percentage for Team 1 --> "))
  return odds

def overtime(ot_number,team1,team2,odds1):
  runs = 0
  while True:
    # check if win
    if team1 == (ot_number*3)+16 or team2 == (ot_number*3)+16:
      ot_score = [team1,team2,ot_number]
      return ot_score
    odds = random.randint(0,100)
    # check for additional overtime
    if team1 == (ot_number*3)+15 and team2 == (ot_number*3)+15:
      ot_number += 1
      print(ot_number)
      ot_score = [team1,team2,ot_number]
      return ot_score
    # give rounds
    elif odds < odds1:
      team1 += 1
    else:
      team2 += 1
    runs += 1
    if runs >= 100:
      print("OVERLOAD")
      break

class battle_odds:
  
  def __init__(self,odds1):
    self.odds1 = odds1
    
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

  def silenced_bo1(self,odds1):
    global ot_number
    ot_number = 1
    team1 = 0 # team 1 rounds
    team2 = 0 # team 2 rounds
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
    if team1 > team2:
      return 1
    else:
      return 2
     
