import os, time

TODO = []

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  date = input("Due Date: ")
  priority = input("Priority: ").capitalize()
  row = [name, date, priority]
  TODO.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n: ")
  if options == "1":
    for row in TODO:
      for item in row:
        print(item, end= " |")
      print()
    print()
  else:
    priority = input("What priority?: ").capitalize()
    for row in TODO:
      if priority in row:
        for item in row:
          print(item, end= " |")
        print()
      print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit: ")
  found = False
  for row in TODO:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in TODO:
    if find in row:
      TODO.remove(row)
  name = input("Name: ")
  date = input("Due Date: ")
  priority = input("Priority: ").capitalize()
  row = [name, date, priority]
  TODO.append(row)
  print("Added")
      

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove: ")
  for row in TODO:
    if find in row:
      TODO.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n: ")
  if menu == "1":
    add()
  elif menu =="2":
    view()
  elif menu =="3":
    edit()
  else:
    remove()
  time.sleep(1)
  os.system("clear")
