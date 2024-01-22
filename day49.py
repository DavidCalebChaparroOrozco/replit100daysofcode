# file = open("high.score", "r")
# contents = file.read()
# file.close()

# print(contents)
# contents = contents.split()
# print(contents)

# file = open("high.score","r")
# contents = file.readline()
# print(contents)
# file.close()

# file = open("high.score","r")
# contents = file.readline().strip()
# print(contents)
# contents = file.readline().strip()
# print(contents)
# contents = file.readline().strip()
# print(contents)
# contents = file.readline().strip()
# print(contents)
# file.close()


# file = open("high.score","r")

# while True:
#   contents = file.readline().strip()
#   if contents == "":
#     break
#   print(contents)

# file.close()


import os, time

file = open("high.score", "r")
score = file.read().split("\n")
file.close()

highscore = 0
name = None

for rows in score:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is: ", name, "with", highscore)
