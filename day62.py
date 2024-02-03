from replit import db
import datetime, os, time

def add():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input(": ")
  db[timestamp] = entry

def view():
  keys = db.keys
  for key in keys:
    time.sleep(1)
    os.systeam("clear")
    print(f"""{key} {db[key]}""")
    print()
    option = input("Next or Exit? :")
    if(option.lower()[0]=="e"):
      break

password = input("Password: ")
if password != "test1":
  print("Incorrect")
  exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n: ")
  if menu == 1:
    add()
  else:
    view()

