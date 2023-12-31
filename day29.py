# for i in range(0, 100):
#   print(i, end=", ")

# print("If you put")
# print("\033[33m", end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")

# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")


# import os, time
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.5)
#   os.system("clear")


# import os, time
# print('\033[?25l', end="")
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.2)
#   os.system("cls")

def Print(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
Print("red", "new program")
Print("reset", " I can just call red('and') ")
Print("red", "it will print in red ")
Print("blue", "or even blue")
