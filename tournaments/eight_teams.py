from match import *
import random

all_matches = []

'''
8 Teams - Single Elimination
Creating all matches
'''

print("instantiating quarter-final matches objects")
for i in range(1,5): # quarter-final matches
  if i % 2 == 0:
    new_match = Match(i,-1, int(i- i/2) +4)
  else:
    new_match = Match(i,-1, int((i+1) - (i+1)/2) +4)
  all_matches.append(new_match)

print("instantiating semi-final matches objects")

new_match = Match(5,-1,7)
all_matches.append(new_match)
new_match = Match(6,-1,7)
all_matches.append(new_match)
  
# grand-final Match
new_match = Match(7,-1,-1)
all_matches.append(new_match)

'''
Functions
'''

# displays the whole bracket vertically
def print_bracket():
  count = 1
  print("Quarter-finals")
  for i in range(4):
    match = all_matches[i]
    match.team1 = f"Team{count}"
    count += 1
    match.team2 = f"Team{count}"
    count += 1
    match.draw()
    
  print("Semi-finals")
  for i in range(4,6):
    all_matches[i].draw()
  
  print("Grand-finals")
  all_matches[6].draw()

# give all matches a random result
def randomize_bracket():
  for i in all_matches:
    i.result = random.randint(1,4)

# get index (for all_matches) for a match with 'id'
def look_for(id):
  ind = 0
  if id == -1:
      return -1
  for i in all_matches:
    if i.input_id == id:
        return ind
      
    ind += 1
  return ind

def update():
  # {team_name: win/lose_id}
  update = {}
  for i in all_matches:
    if i.result != 0 and i.team1 != "Empty":
      if i.result <= 2: # team 1 win
        update [i.team1] = i.winner_id
        update [i.team2] = i.loser_id
      elif i.result <= 4: # team 2 win
        update [i.team2] = i.winner_id
        update [i.team1] = i.loser_id

  for key, value in update.items():
    index = look_for(value)
    if index != -1:
      if all_matches[index].team1 == "Empty":
        all_matches[index].team1 = key
      else:
        all_matches[index].team2 = key
      
    
randomize_bracket()

print_bracket()

update()
print_bracket()

update()
print_bracket()