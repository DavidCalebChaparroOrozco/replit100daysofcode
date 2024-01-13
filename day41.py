# myDictionary = {
#   "name" : "Ian", 
#   "health": 219, 
#   "strength": 199, 
#   "equipped": "Axe"
#   }

# for i in myDictionary:
#   print(myDictionary[i])

# for value in myDictionary.values():
#   print(value)

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")

# for name, value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     print("Whoa, SO STRONG!")


# myDictionary = {
#   "name": "David the Mildy Terrifying",
#   "health": 186,
#   "strength": 4,
#   "equipped": "l33t haxx0r p0werz"
# }
# for name, value in myDictionary.items():
#   print(f"{name}:{value}")
#   if (name == "strength"):
#     if value > 100:
#       print("Whoa, SO STRONG")
#     else:
#       print(
#         "Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!"
#       )


# myDictionary = {
#   "name": "Ian",
#   "health": 219,
#   "strength": 199,
#   "equipped": "Axe"
# }

# for name, value in myDictionary.items():
#   print(f"{name} {value}")


# myDictionary = {
#   "name": "David the Mildy Terrifying",
#   "health": 186,
#   "strength": 4,
#   "equipped": "l33t haxx0r p0werz"
# }

# for name, value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     if value > 100:
#       print("Whoa, SO STRONG")
#   else:
#     print(
#       "Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!"
#     )


website = {"name": None, "url": None, "desc": None, "rating": None}
for name in website.keys():
  website[name] = input(f"{name}: ")
for name, value in website.items():
  print(f"{name}: {value}")
