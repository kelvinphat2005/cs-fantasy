from old.randombattle import *
from old.odds import *

global team1odds

def random_menu():
  while True:
    i = input("[1] BO1 [2] BO3 [3] BO5 [4] Exit--> ")
    if i == "1":
      ddd = 0
      while ddd < 5:
        bo1()
        ddd += 1
    elif i == "2":
      ddd = 0
      while ddd < 3:
        bo3()
        ddd += 1
    elif i == "3":
      bo5()
    elif i == "4":
      break
    else:
      print("Unknown Command")

def odds_menu():
  team1odds = 50
  while True:
    i = input("[1] BO1 [2] BO3 [3] BO5 [4] Edit odds [5] Exit--> ")
    odds_battle = battle_odds(team1odds)
    if i == "1":
      odds_battle.bo1(team1odds)

    elif i == "2":
      team1maps = 0
      team2maps = 0
      i = 0
      while i <= 3:
        if odds_battle.silenced_bo1(team1odds) == 1:
          team1maps += 1
        else:
          team2maps += 1
        if team1maps == 2 or team2maps == 2:
          break
        i += 1
      print("Best of 3:\n" + str(team1maps) + " - " + str(team2maps))

    elif i == "3":
      team1maps = 0
      team2maps = 0
      i = 0
      while i <= 5:
        if odds_battle.silenced_bo1(team1odds) == 1:
          team1maps += 1
        else:
          team2maps += 1
        if team1maps == 3 or team2maps == 3:
          break
        i += 1
      print("Best of 3:\n" + str(team1maps) + " - " + str(team2maps))

    elif i == "4":
      team1odds = edit_odds()
      print("Team 1 odds are now: " + str(team1odds))
    elif i == "5":
      break
    else:
      print("Unknown Command")

def main_menu():
  while True:
    i = input("[1] MAIN [2] Random [3] Custom Odds [4] Exit --> ")
    if i == "1":
      main()
    elif i == "2":
      random_menu()
    elif i == "3":
      odds_menu()
    elif i == "4":
      break

main_menu()