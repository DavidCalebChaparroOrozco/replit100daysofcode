# listOfShame = []
# while True:
#   name = input("What is your name?: ")
#   age = int(input("What is your age?: "))
#   pref = input("What is your computer platform?: ")
#   row = [name, age, pref]
#   listOfShame.append(row)
#   exit = input("Exit? y/n: ")
#   if (exit.strip().lower()[0] == "y"):
#     break
# def prettyPrint():
#   print()
#   for row in listOfShame:
#     for item in row:
#       print(f"{item:^10}", end=" | ")
#       print()
# prettyPrint()


# listOfShame = [] 
# while True: 
#   menu = input("Add or Remove?") 
#   if(menu.strip().lower()[0]=="a"): 
#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")
#     row = [name, age, pref] 
#     listOfShame.append(row)
#     exit = input("Exit? y/n: ")
#     if (exit.strip().lower()[0] == "y"):
#       break
#   else: 
#     for row in listOfShame:
#       if name in row:
#         listOfShame.remove(row)
# def prettyPrint():
#   print()
#   for row in listOfShame:
#     for item in row:
#       print(f"{item:^10}", end=" | ")
#       print()
# prettyPrint()


import random, os, time
bingo = []
def ran():
  num = random.randint(1, 90)
  return num
def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()
def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  numbers.sort()
  bingo = [[numbers[0], numbers[1], numbers[2]],
           [numbers[3], "BINGO", numbers[4]],
           [numbers[5], numbers[6], numbers[7]]]
createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"
  exes = 0
  for row in bingo:
    for item in row:
      if item == "X":
        exes += 1
  if exes == 8:
    print("You have won!")
    break
  time.sleep(1)
  os.system("clear")
