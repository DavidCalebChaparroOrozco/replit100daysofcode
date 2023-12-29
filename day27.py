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

while True:
  print("Welcome to the Dungeon Crawler")
  name = input("Enter your name: ")
  type = input("Character type (Human, Orc, Elf, Dwarf, Halfling, Dragonborn, Gnome): ")
  print(name)
  print("HP: ", health())
  print("STR: ", strength())
  play = input("Again? (y/n): ")
  if play == "n":
    break
  time.sleep(1)
  os.system("clear")
