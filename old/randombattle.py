import random

ot_number = 1

def overtime(ot_number,team1,team2):
  runs = 0
  while True:
    # check if win
    if team1 == (ot_number*3)+16 or team2 == (ot_number*3)+16:
      ot_score = [team1,team2,ot_number]
      return ot_score
    odds = random.randint(0,1)
    # check for additional overtime
    if team1 == (ot_number*3)+15 and team2 == (ot_number*3)+15:
      ot_number += 1
      print(ot_number)
      ot_score = [team1,team2,ot_number]
      return ot_score
    # give rounds
    elif odds == 0:
      team1 += 1
    else:
      team2 += 1
    runs += 1
    if runs >= 100:
      print("OVERLOAD")
      break

def bo1():
  print("Best of 1: ")
  global ot_number
  ot_number = 1
  team1 = 0
  team2 = 0
  while team1 <= (ot_number*3)+12 and team2 <= (ot_number*3) + 12:
    odds = random.randint(0,1)
    # check for overtime
    if team1 >= (ot_number*3) + 12 and team2 >= (ot_number*3) + 12:
      score = overtime(ot_number,team1,team2)
      team1 = score[0]
      team2 = score[1]
      ot_number = score[2]
    # add score if not overtime
    else: 
      if odds == 0:
        team1 += 1
      else:
        team2 += 1
  print(str(team1) + " - " + str(team2))
  return

def bo3():
  print("Best of 3: ")
  team1 = 0
  team2 = 0
  while team1 < 2 and team2 < 2:
    odds = random.randint(0,1)
    if odds == 0:
      team1 += 1
    else:
      team2 += 1
  print(str(team1) + " - " + str(team2))
  return

def bo5():
  print("Best of 5: ")
  team1 = 0
  team2 = 0
  while team1 < 3 and team2 < 3:
    odds = random.randint(0,1)
    if odds == 0:
      team1 += 1
    else:
      team2 += 1
  print(str(team1) + " - " + str(team2))
  return