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
    self.openingrate = openingrate # use later
    self.riflerating = riflerating
    self.pistolrating = pistolrating # use later
    self.hs = hs
    self.awp = awp
    self.awprating = awprating

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
      print(player)
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


    def __repr__(self):
      return f"Players('{self.name}',{self.money},{self.firepower},{self.openingwin},{self.openingrate},{self.riflerating},{self.pistolrating},{self.hs},{self.awp},{self.awprating})"

# Players.instantiate_from_csv()
# print(Players.all[1].name)