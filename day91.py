import requests, json, os, time
from replit import db

while True:
  time.sleep(1)
  os.system("clear")
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) # get a random dad joke from the site endpoint and assign to a variable. The second argument (the header request) tells the script to return the json data as a string.

  joke = result.json()
  # print(json.dumps(joke, indent=2))
  # print(joke["joke"])

  jk = joke["joke"]
  id = joke["id"]
  print(jk)

  answer = int(input("\n1. Save joke, 2. Load old jokes, 3. New Joke\n"))
  if answer == 1:
    continue
  elif answer == 2:
    db[id] = jk
    print("\nSAVED\n")
    continue
  elif answer == 3:
    keys = db.keys()
    for key in keys:
      result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept":"application/json"})
      joke = result.json()
      print(joke["joke"])
      print("\n")
      time.sleep(1)
  else:
    print("The option is incorrect, try it again.")
