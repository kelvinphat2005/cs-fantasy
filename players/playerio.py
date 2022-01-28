def readplayer(player):
  value = []
  file = open("players/" + player + ".txt","r")
  value = file.readlines()

  # removing /n
  count = 0
  for i in value:
    value[count] = i.strip()
    count += 1

  file.close()
  return value

def writeplayer(player,input_list):
  file = open("players/" + player + ".txt", "w")
  for i in input_list:
    file.write(i + "\n")
  file.close()
  return