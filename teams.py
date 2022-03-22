import csv

class Teams():

  all = []
  
  def __init__(self,name,player1,player2,player3,player4,player5):
    print(f"Created team {name}")
    # Validations
    # assert money >= 0, f"Money of {money} cannot be negative"
    
    # Initialize
    self.__name = name
    self.__player1 = player1
    self.__player2 = player2
    self.__player3 = player3
    self.__player4 = player4
    self.__player5 = player5

    Teams.all.append(self)
    return

  @property # Property Decorator = Read-only Attribute
  def name(self):
    return self.__name

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


    def __repr__(self):
      return f"Team('{self.name}',{self.player1})"

Teams.instantiate_from_csv()