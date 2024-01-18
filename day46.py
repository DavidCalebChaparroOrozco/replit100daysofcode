# clue = {}
# def prettyPrint():
#   print()
#   for key, value in clue.items():
#     print(key, end=": ")
#     for subKey, subValue in value.items():
#       print(subKey, subValue, end=" | ")
#     print()
# prettyPrint()
# while True:
#   name = input("Enter your name: ")
#   location = input("Enter your location: ")
#   weapon = input("Enter your weapon: ")
#   clue[name] = {"location": location, "weapon": weapon}
#   print(clue)


# maxi = {"daysCompleted": 46, "streak": 22}
# andrea = {"daysCompleted": 21, "streak": 12}
# alonso = {"daysCompleted": 75, "streak": 6}
# courseProgress = {"Max": maxi, "Andrea": andrea, "Alonso": alonso}
# #print(courseProgress)
# print(courseProgress["Alonso"]["daysCompleted"])


import os, time
mokedex = {}
def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"
    ]:^6}""")
while True:
  print("Add your Beast!")
  name = input("Name :").title()
  type = input("Type :").title()
  hp = int(input("HP :"))
  mp = int(input("MP :"))
  mokedex[name] = {"type": type, "hp": hp, "mp": mp}
  print(" ".center(50,"-"))
  print()
  prettyPrint()
