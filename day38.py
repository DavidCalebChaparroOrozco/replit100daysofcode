# myString = "Day 38"
# for letter in myString:
#   print(letter)

# #D
# #a
# #y
# # 
# #3
# #8


# myString = "Day 38"
# for letter in myString:
#   if letter.lower() == "a":
#     print('\033[33m', end='')  #yellow
#   print(letter)
#   print('\033[0m', end='')  #back to default

# # This code outputs (with a yellow 'a'):
# #D
# #a
# #y
# #
# #3
# #8


# myString = "Day 38"
# for letter in myString:
#   if letter.lower() == "a":
#     print('\033[33m', end='')  #yellow
#   print(letter)
#   print('\033[0m', end='')  #back to default

# # This code outputs (with a yellow 'a'):
# #D
# #a
# #y
# #
# #3
# #8


# vowels = ["a","e","i","o","u"]
# myString = "Will my vowels now be yellow?"
# for letter in myString:
#   if letter.lower() in vowels:
#     print('\033[33m', end='') #yellow
#   print(letter, end="")
#   print('\033[0m', end='') #back to default


def colorChange(color):
  if color=="r":
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[34m", end="")
  elif color=="y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")

sentence = input("What sentence do you want rainbow-izing?: ")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()
