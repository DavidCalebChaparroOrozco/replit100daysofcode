# import random

# def pinPicker(number):
#   pin = ""
#   for i in range(number):
#     pin += str(random.randint(0, 9))
#   return pin
# myPin = pinPicker(4)
# print(myPin)


# def areaOfTriangle(base, height):
#   area = 0.5 * base * height
#   return area
# area= areaOfTriangle(5, 22)
# print(area)


# def area_square(side1, side2):
#   area = side1 * side2
#   return area
# area= area_square(4, 12)
# print(area)


import random

def rollDice(sides):
  dice = random.randint(1, sides)
  return dice

def roll_6_and_8():
  roll_6_sides_dice = rollDice(6)
  roll_8_sides_dice = rollDice(8)
  health = roll_6_sides_dice * roll_8_sides_dice
  return health

print("Character stats generator")

play = "yes"

while play == "yes":
  name = input("Enter the name of the warrior: ")
  hp = str(roll_6_and_8())
  print(f"{name} has {hp} hp")
  play = input("Do you want to play again? (yes/no): ")
