import os, time, random


def add():
  os.system("clear")
  idea = input("Idea: ")
  file = open("my.ideas", "a+")
  file.write(f"{idea}\n")
  file.close()
  time.sleep(1)
  os.system("clear")


def show():
  os.system("clear")
  file = open("my.ideas", "r")
  ideas = file.read().split("\n")
  file.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")


while True:
  menu = input("1: Add idea\n2: Show a random idea\n> ")
  if menu == "1":
    add()
  else:
    show()
