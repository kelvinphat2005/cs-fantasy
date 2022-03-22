print("Player Creation:")
# Team Name
playername = input("Player Name --> ").lower()
# Opening Kills
openingwin = input("Opening Kill Winrate % --> ")
openingrate = input("Opening chance % --> ")
# Overall
riflerating = input("Rifle Rating --> ")
pistolrating = input("Pistol Rating --> ")
ecorating = input("Eco Round Rating --> ")
hs = input("Headshot Percentage --> ")
# AWP
awp = input("Awper? [0/1] --> ")
awprating = input("Awp Rating --> ")
# Support
# supportrating = input("Support Rating --> ")
# iglrating = input("IGL Rating --> ")

# add team properties
f = open("players/" + playername + ".txt", "w")
f.write(playername + "\n")
f.write(openingwin + "\n")
f.write(openingrate + "\n")
f.write(riflerating + "\n")
f.write(pistolrating+ "\n")
# f.write(ecorating + "\n")
f.write(hs + "\n")
f.write(awp + "\n")
f.write(awprating + "\n")
f.close()

# add team to the team list
f = open("players/playerlist.txt", "a")
f.write(playername + "\n")
f.close()