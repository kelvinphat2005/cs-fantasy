# debugging player.__dict__
import csv

class Players():

  all = []
  
  def __init__(self,name: str,money,firepower,openingwin,openingrate,riflerating,pistolrating,hs,awp,awprating):
    print(f"Created player {name}")
    # Validations
    # assert money >= 0, f"Money of {money} cannot be negative"
    
    # Initialize
    self.__name = name
    self.__money = money
    self.__firepower = firepower
    self.__openingwin = openingwin # use later
    self.__openingrate = openingrate # use later
    self.__riflerating = riflerating
    self.__pistolrating = pistolrating # use later
    self.__hs = hs
    self.__awp = awp
    self.__awprating = awprating

    Players.all.append(self)
    return

  @property # Property Decorator = Read-only Attribute
  def name(self):
    return self.__name

  @property
  def money(self):
    return self.__money

  @property
  def firepower(self):
    return self.__firepower
  
  @property
  def openingwin(self):
    return self.__openingwin

  @property
  def openingrate(self):
    return self.__openingrate
  
  @property
  def riflerating(self):
    return self.__riflerating

  @property
  def pistolrating(self):
    return self.__pistolrating

  @property
  def hs(self):
    return self.__hs

  @property
  def awp(self):
    return self.__awp

  @property
  def awprating(self):
    return self.__awprating


  @money.setter
  def money(self,value):
    self.money = value

  @firepower.setter
  def firepower(self,value):
    self.firepower = value
  
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
        openingwin=float(player.get("openingwin")),
        openingrate=float(player.get("openingrate")),
        riflerating=float(player.get("riflerating")),
        pistolrating=float(player.get("pistolrating")),
        hs=float(player.get("hs")),
        awp=IndentationError(player.get("awp")),
        awprating=float(player.get("awprating")),
      )

  @staticmethod
  def add_player():
    create_player()
  
  def __repr__(self):
    return f"Players('{self.name}',{self.money},{self.firepower},{self.openingwin},{self.openingrate},{self.riflerating},{self.pistolrating},{self.hs},{self.awp},{self.awprating})"

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