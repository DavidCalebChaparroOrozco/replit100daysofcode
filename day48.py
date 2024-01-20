# file = open("savedFile.txt", "w")

# # file.write("Hello World")
# # file.close()

# # Text = input(": ")
# # file.write(Text)
# # file.close()


# file = open("savedFile.txt", "a+")
# Text = input(": ")
# file.write(f"{Text}\n")
# NewText = input(": ")
# file.write(f"{NewText}\n")
# file.close()


import os, time

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("Enter your initials: ").upper()
  score = int(input("Enter your score: "))
  print()
  
  file = open("high.score", "a+")
  file.write(f"{name} {score}\n")
  file.close()
  
  print("Added to high score table.")
  time.sleep(1)
  os.system("clear")
