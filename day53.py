import os, time

inventary = []

try:
  file = open("inventary.txt", "r")
  inventary = eval(file.read())
  file.close()
except:
  pass

def addItem():
  time.sleep(1)
  os.system("clear")
  print(" INVENTORY ".center(50,"-"))
  print()
  item = input("Item to add: ").capitalize()
  inventary.append(item)
  print("Added")

def viewItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY".center(50,"-"))
  seen = []
  for item in inventary:
    if item not in seen:
      print(f"{item} : {inventary.count(item)}")
      seen.append(item)
  time.sleep(2)

def removerItem():
  time.sleep(1)
  os.system("clear")
  print(" INVENTORY ".center(50,"-"))
  print()
  item = input("Item to remove: ").capitalize()
  if item in inventary:
    inventary.remove(item)
    print("Removed")
  else:
    print("You don't have that item")

while True:
  time.sleep(1)
  os.system("clear")
  print(" INVENTORY ".center(50,"-"))
  print()
  menu = int(input("1: Add\n2: View\n3: Remove\n> "))
  if menu == 1:
    addItem()
  elif menu == 2:
    viewItem()
  else:
    removerItem()
