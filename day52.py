# debugMode = True
# myStuff = []

# try:
#   file.open("Stuff.mine","r")
#   myStuff = eval(file.read())
#   file.close()
# # Try to find a file called 'Stuff.mine' and open it

# except Exception as err:
#   print("ERROR: Unable to load")
#   print(err)
# # If the file can't be found, show the error instead of crashing the whole program

#   if debugMode:
#     print(traceback)
    
# for row in myStuff:
#   print(row)


import os, time

pizza = []

try:
  file = open("pizza.txt", "r")
  pizza = eval(file.read())
  file.close()
except:
  print("Error: No existing pizza list, using a blank list")

def viewPizza():
  Name = "Name"
  Topping = "Topping"
  Size = "Size"
  Quantity = "Quantity"
  Total = "Total"
  print(f" {Name:^10} {Topping:^20} {Size:^10} {Quantity:^10} {Total:^10}")
  for row in pizza:
    print(f" {row[0]:^10} {row[1]:^20} {row[2]:^10} {row[3]:^10} {row[4]:^10}")
    time.sleep(2)

def addPizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  toppings = input("Toppings: ")
  size = input("Size (s/m/l): ").lower()
  while True:
    try:
      quantity = int(input("Quantity: "))
      break
    except:
      print("Error: Quantity must be a whole number")
  cost = 0
  if size == "s":
    cost = 5.99
  elif size == "m":
    cost = 9.99
  else:
    cost = 14.99
  total = cost * quantity
  total = round(total, 2)
  row = [name, toppings, size, quantity, total]
  pizza.append(row)

while True:
  time.sleep(1)
  os.system("clear")
  print("🌟Caleb's Dodgy Pizzas🌟")
  print()
  menu = input("1: Add Pizza\n2: View Pizzas\n> ")
  if menu == "1":
    addPizza()
  else:
    viewPizza()
  time.sleep(1)
  os.system("clear")
  file = open("pizza.txt", "w")
  file.write(str(pizza))
  file.close()
