# import os

# print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.

# files = os.listdir()
# if "quickSave.txt" not in files:
#   print("Error: Quick Save not found.")
# #Checks if a file is in a directory and outputs an error if not.


# import os

# os.mkdir("Hello") # Creates a folder called 'Hello'

# os.rename("Caleb.txt", "NEW.o")



import os, time, random

TODO = []

fileExists = True

try:
  file = open("TO.DO", "r")
  TODO = eval(file.read())
  file.close()

except:
  fileExists = False

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name:")
  date = input("Due Date:")
  priority = input("Priority:").capitalize()
  row = [name, date, priority]
  TODO.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = int(input("1: All\n2: By Priority\n> "))
  if options == 1:
    for row in TODO:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority: ").capitalize()
    for row in TODO:
      if priority in row:
        for item in row:
          print(item, end=" | ")
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
    print("Could't find that")
    return
  for row in TODO:
    if find in row:
      TODO.remove(row)
  name = input("Name:")
  date = input("Due Date:")
  priority = input("Priority:").capitalize()
  row = [name, date, priority]
  TODO.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of TODO to remove: ")
  for row in TODO:
    if find in row:
      TODO.remove(row)

while True:
  menu = int(input("1: Add\n2: View\n3: Edit\n4: Remove\n> "))
  if menu == 1:
    add()
  elif menu == 2:
    view()
  elif menu == 3:
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")

  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass
    name = f"backup{random.randint(1,1000000000)}.txt"

  file = open("TO.DO", "w")
  file.write(str(TODO))
  file.close()
