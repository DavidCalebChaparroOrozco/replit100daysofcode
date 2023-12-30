import random, os, time

def roll_dice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStats = ((roll_dice(6)*roll_dice(12))/2)+10
  return healthStats

def strength():
  strengthStat = ((roll_dice(6)*roll_dice(8))/2)+12
  return strengthStat


print("Welcome to the Dungeon Crawler")
c1name = input("Enter your name: ")
c1type = input("Character type (Human, Orc, Elf, Dwarf, Halfling, Dragonborn, Gnome): ")
c1hp = health()
c1str = strength()
print(c1name)
print("HP: ", c1hp)
print("STR: ", c1str)

print("You wake up in a dark cave")
print("Who are they battling?")

c2name = input("Enter your opponent's name: ")
c2type = input("Character type (Human, Orc, Elf, Dwarf, Halfling, Dragonborn, Gnome): ")
c2hp = health()
c2str = strength()
print(c2name)
print("HP", c2hp)
print("STR: ", c2str)

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("The battle begins!")
  
  c1Dice = roll_dice(6)
  c2Dice = roll_dice(6)
  
  difference = abs(c1str - c2str)+1
  
  if c1Dice > c2Dice:
    c2hp -= difference
    if round == 1:
      print(c1name, "Win the first blow")
    else:
      print(c1name,"wins round", round)
  elif c2Dice > c1Dice:
    if round == 1:
      print(c2name, "Win the first blow")
    else:
      print(c2name,"wins round", round)
  else:
    print("Draw!", round)

  print(c1name)
  print("HP: ", c1hp)
  print(c2name)
  print("HP: ", c2hp)
  if c1hp <= 0:
    print(c1name, "has been defeated")
    winner = c2name
    break
  elif c2hp <= 0:
    print(c2name, "has been defeated")
    winner = c1name
    break
  else: 
    print("And they're both standing for the next round")
    round += 1

time.sleep(1)
os.system("clear")
print(winner, "has won in", round, "rounds!")
