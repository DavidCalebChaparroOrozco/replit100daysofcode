from replit import db

# db["test"] = "Hello there"

# keys = db.keys()
# print(keys)

# value = db["test"]
# print(value)

# del db["test"]


# db["login1"] = "Caleb"
# db["login2"] = "David"
# db["login3"] = "Maximiliano"
# db["login4"] = "Andrea"

# matches = db.prefix("login")
# print(matches)


# db["david"] = {"username": "dmorgan", "password":"baldy1"}

# keys = db.keys()
# print(keys)

# value = db["david"]
# print(value["password"])

# keys = db.keys()
# for key in keys:
#   print(f"""{key}: {db[key]}""")


from replit import db
import datetime, os, time


def addTweet():
  tweet = input("Enter your tweet: ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")


def viewTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter += 1
    if (counter % 10 == 0):
      carryOn = input("Next 10?: ")
      if (carryOn.lower() == "no"):
        break
  time.sleep(1)
  os.system("clear")


while True:
  print("Tweeter")
  menu = int(input("1: Add Tweet\n2: View Tweets\n: "))
  if menu == 1:
    addTweet()
  else:
    viewTweet()
