# Events = []

# def prettyPrint():
#   print()
#   for row in Events:
#     print(f" {row[0] :^15} {row[1] :^15}")
#   print()

# while True:
#   menu = input("1: Add, 2: Remove\n")
  
#   if menu == "1":
#     event = input("What event?: ").capitalize()
#     date = input("What date?: ")
#     row = [event,date]
#     Events.append(row)
#     prettyPrint()

#   else:
#     criteria = input("What event do you want to remove?: ").title()
#     for row in Events:
#       if criteria in row:
#         Events.remove(row)
#     prettyPrint()

#   file = open("calendar.txt","w")

#   file.write(str(Events))

#   file.close()



# Events = []

# ####### THIS IS THE NEW BIT ################
# file = open("calendar.txt", "r")  # Only need read permissions here
# Events = eval(file.read())
# file.close()
# ########################################


# def prettyPrint():
#   print()
#   for row in Events:
#     print(f"{row[0] :^15} {row[1] :^15}")
#   print()


# while True:
#   menu = input("1: Add, 2: Remove\n")

#   if menu == "1":
#     event = input("What event?: ").capitalize()
#     date = input("What date?: ")
#     row = [event, date]
#     Events.append(row)
#     prettyPrint()

#   else:
#     criteria = input("What event do you want to remove?: ").title()
#     for row in Events:
#       if criteria in row:
#         Events.remove(row)

#   file = open("calendar.txt", "w")
#   file.write(str(Events))
#   file.close()



# Events = []

# def prettyPrint():
#   print()
#   for row in Events:
#     print(f"{row[0] :^15} {row[1] :^15}")
#   print()

# while True:
#   menu = input("1: Add, 2: Remove\n")

#   if menu == "1":
#     event = input("What event?: ").capitalize()
#     date = input("What date?: ")
#     row = [event,date]
#     Events.append(row)
#     prettyPrint()

#   else:
#     criteria = input("What event do you want to remove?: ").title()
#     for row in Events:
#       if criteria in row:
#         Events.remove(row)

  
# file = open("calendar.txt", "w") 
# file.write(str(Events)) 
# file.close()


import os, time

TODO = []
file = open("TO_DO.TXT", "r")
file.close()

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
  options = int(input("1: All\n2: By Priority\n> "))
  if options == 1:
    for row in TODO:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority?: ").capitalize()
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
  find = input("Name of TODO to edit: ")
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
  file = open("TO_DO.txt", "w")
  file.write(str(TODO))
  file.close()
