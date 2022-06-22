# debugging player.__dict__
import csv

class Players():

  all = []
  
  def __init__(self,name: str,money,firepower,riflerating,pistolrating,awprating,gun,awp):
    print(f"Created player {name}")
    # Validations
    # assert money >= 0, f"Money of {money} cannot be negative"
    
    # Initialize
    self.name = name
    self.money = money
    self.firepower = firepower
    self.riflerating = riflerating
    self.pistolrating = pistolrating
    self.awprating = awprating
    self.gun = gun
    self.awp = awp

    Players.all.append(self)
    return

  def set_team(self, team_name):
    self.team = team_name
  
  @classmethod
  def instantiate_from_csv(cls): # load all players from csv file
    with open("players.csv", "r") as f:
      reader = csv.DictReader(f)
      players = list(reader)

    for player in players:
      Players(
        name=player.get("name"),
        money=float(player.get("money")),
        firepower=float(player.get("firepower")),
        riflerating=float(player.get("riflerating")),
        pistolrating=float(player.get("pistolrating")),
        awprating=float(player.get("awprating")),
        gun=player.get("gun"),
        awp=IndentationError(player.get("awp")),
      )

  @staticmethod
  def add_player():
    create_player()
  
  def __repr__(self):
    return f"Players('Name: {self.name},Money: {self.money},Firepower: {self.firepower},Rifle Rating: {self.riflerating},Pistol Rating:{self.pistolrating},AWP Rating: {self.awprating},Gun: {self.gun},AWP: {self.awp}')"

def create_player():
  print("ADD PLAYER MENU")
  current_prompt = 0
  prompts = ("Player Name","Opening Rating","Opening Attempt Rate","Rifle Rating","Pistol Rating","Headshot %","AWPer?","AWP Rating")
  new_player = []
  # Getting Values
  i = input(f"{prompts[current_prompt]} --> ") # Team Name
  new_player.append(i)
  current_prompt += 1
  while current_prompt < len(prompts):
    try:
      i = float(input(f"{prompts[current_prompt]} --> "))
    except ValueError:
      print("Input Number")
      break
      
    # checking if float
    if isinstance(i, float): 
      current_prompt += 1
      i = str(i)
      new_player.append(i)

  # adding money and firepower to new_player
  new_player.insert(1,"1") # fp
  new_player.insert(1,"800") # money
  
  # adding new player to players.csv
  with open("players.csv","a") as f:
    f.write("\n"+",".join(new_player).strip(""))

  return

'''Players.instantiate_from_csv()
print(Players.all)'''