class Match:

  def __init__(self, input_id, loser_id, winner_id):
    self.team1 = "Empty"
    self.team2 = "Empty"
    # 0 = 0 - 0, 1 = 2 - 0, 2 = 2 - 1, 3 = 0 - 2, 4 = 1-2
    self.result = 0
    self.input_id = input_id # if -1 then win
    self.loser_id = loser_id # if -1 then eliminated
    self.winner_id = winner_id

  def __str__(self):
    return f"input id: {self.input_id} loser_id: {self.loser_id} winner_id: {self.winner_id}"
    
  # Check who is the winner
  def check(self):
    if self.result != 0:
      if self.result < 3:
        # team 1 win
        return 1
      elif self.result < 5:
        # team 2 win
        return 2
      else:
        print("Error")
        return

  def draw(self):
    score = [0,0]
    if self.result == 1:
      score = [2,0]
    elif self.result == 2:
      score = [2,1]
    elif self.result == 3:
      score = [0,2]
    elif self.result == 4:
      score = [1,2]
    else:
      score = [0,0]
      
    print("---------------------")
    print(f"|{self.team1} {(14 - len(self.team1)) * ' '}| {score[0]} |")
    print(f"|{self.team2} {(14 - len(self.team2)) * ' '}| {score[1]} |")
    print("---------------------")
    print(f"input id: {self.input_id} loser_id: {self.loser_id} winner_id: {self.winner_id}")
  
  def set_result(self,new_result):
    self.result = new_result
    return

  def set_team1(self,team):
    self.team1 = team
    return

  def set_team2(self,team):
    self.team2 = team
    return



