import os, time, random
from replit import db
# password = "baldy1"
# password = hash(password)
# print(password)

# userName = "caleb"
# password = "caleb1"
# password = hash(password)
# db[userName] = password

# print(password)
# print(db[userName])


# ask = input("Password: ")
# ask = hash(ask)
# if ask == db["caleb"]:
#   print("Login successful")


# password = "caleb1"
# salt = 10221
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)
# print(newPassword)


# password = "caleb1"
# salt = 10221
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)
# print(newPassword)
# password = "caleb1"
# salt = 39820
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)
# print(newPassword)


# password = "caleb1"
# salt = 10221
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)
# print(newPassword)
# db["caleb"] = {"password":newPassword, "salt":salt}



# ans = input("Password: ")
# salt = db["caleb"]["salt"]# Get the salt from the database.

# newPassword = f"{ans}{salt}"
# newPassword = hash(newPassword)# Hash the concatenated string

# if newPassword == db["caleb"]["password"]: #compare hash of newPassword to stored hash.
#   print("Login successful")


def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000,9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  db[username] = {"password": newPassword, "salt": salt}

  print("User added")

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return

  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[username]["password"]==newPassword:
    print("Logged in")
  else:
    print("Username or password incorrect")

while True:
  menu = int(input("1: New User\n2: Login\n> "))
  if menu == 1:
    createUser()
  elif menu ==2:
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])
