print("Team Creation:")
# Team Name
teamname = input("Team Name --> ").lower()
# Team Rating
# teamrating = input("Team Rating --> ")

# add team properties
f = open("teams/" + teamname + ".txt", "w")
f.write(teamname + "\n")
# f.write(teamrating + "\n")
# empty space for players + stats
i = 1
while i <=12:
  f.write("\n")
  i += 1
f.close()

# add team to the team list
f = open("teams/teamlist.txt", "a")
f.write(teamname + "\n")
f.close()