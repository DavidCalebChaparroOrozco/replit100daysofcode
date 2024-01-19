import os, time, random

trumps = {}
trumps["Vladictor"] = {
  "Intelligence": 170,
  "Speed": 40,
  "Guile": 80,
  "Baldness Level": 0
}
trumps["DEKAN0"] = {
  "Intelligence": 200,
  "Speed": 50,
  "Guile": 50,
  "Baldness Level": 10
}
trumps["Ryu"] = {
  "Intelligence": 170,
  "Speed": 45,
  "Guile": 100,
  "Baldness Level": 20
}
while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Pick your character\n: ")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)
  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")
  answer = input(": ")
  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[user][answer]}")
  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")
  time.sleep(2)
  os.system("clear")
