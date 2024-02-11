import os

# password = os.environ['password'] # Uses the os library to talk to the environment and get the secret password stored there.

# userPass = input("Password: ")
# if userPass == password:
#   print("Well done")
# else:
#   print("Better luck next time")

while True:
  username = input("Username: ")
  password = input("Password: ")
  if username == os.environ['admin'] and password == os.environ['adminPassword']:
    print("Welcome Admin!")
    break
  elif username == os.environ['user'] and password == os.environ['userPassword']:
    print("Welcome User!")
    break
  else:
    print("Try again")
