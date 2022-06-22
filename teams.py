import csv

class Teams():

  all = []
  
  def __init__(self,name,player1,player2,player3,player4,player5):
    print(f"Created team {name}")
    # Validations
    # assert money >= 0, f"Money of {money} cannot be negative"
    
    # Initialize
    self.name = name
    self.player1 = player1
    self.player2 = player2
    self.player3 = player3
    self.player4 = player4
    self.player5 = player5

    Teams.all.append(self)
    return
  
  @classmethod
  def instantiate_from_csv(cls): # load all players from csv file
    with open("teams.csv", "r") as f:
      reader = csv.DictReader(f)
      teams = list(reader)

    for team in teams:
      print(team)
      Teams(
        name=team.get("name"),
        player1=team.get("player1"),
        player2=team.get("player2"),
        player3=team.get("player3"),
        player4=team.get("player4"),
        player5=team.get("player5"),
      )

  @staticmethod
  def add_team():
    create_team()
  
  def __repr__(self):
    return f"Team('{self.__name}',{self.__player1})"

def create_team():
  print("ADD TEAM MENU")
  current_prompt = 0
  prompts = ("Team Name [NO SPACES]","Player 1 Name","Player 2 Name","Player 3 Name","Player 4 Name","Player 5 Name")
  new_team = []
  # Getting Values
  while current_prompt < len(prompts):
    i = input(f"{prompts[current_prompt]} --> ") # Team Name
    new_team.append(i)
    current_prompt += 1

  # adding new player to players.csv
  with open("teams.csv","a") as f:
    f.write("\n"+",".join(new_team).strip(""))

  return

# Teams.instantiate_from_csv()