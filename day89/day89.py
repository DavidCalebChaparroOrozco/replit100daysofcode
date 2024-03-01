from flask import Flask, request, redirect
import datetime
from replit import db

app = Flask('app')


@app.route('/')
def index():
  page = ""
  file = open("chat.html", "r")
  page = file.read()
  file.close()
  page = page.replace("{username}", request.headers["X-Replit-User-Name"])
  page = page.replace("{chats}", getChat(request.headers["X-Replit-User-Name"]))
  return page


@app.route("/add", methods=["POST"])
def add():
  form = request.form
  message = form["message"]
  date = datetime.datetime.now()
  timestamp = datetime.datetime.timestamp(date)
  userId = request.headers["X-Replit-User-Id"]
  userName = request.headers["X-Replit-User-Name"]
  db[timestamp] = {"userId": userId, "userName": userName, "message": message}
  #page = f"""{userId} {userName} {timestamp} {message}"""
  return redirect("/")


def getChat(user):
  message = ""
  file= open("message.html","r")
  message = file.read()
  file.close()
  keys = db.keys()
  keys = list(keys)
  result = ""
  recent = 0
  for key in reversed(keys):
    #print(db[key]["userId"])
    myMessage = message
    myMessage = myMessage.replace("{username}", db[key]["userName"])
    myMessage = myMessage.replace("{timestamp}", key)
    myMessage = myMessage.replace("{message}", db[key]["message"])
    if db[key]["userName"] == "David-CalebCale":
      myMessage = myMessage.replace("{admin}",f"""<a href="/delete?id={key}">✖️</a>""")
    else:
      myMessage = myMessage.replace("{admin}","")
    result += myMessage
    recent += 1
    if recent == 5:
      break
  return result


@app.route("/delete", methods=["GET"])
def delete():
  if request.headers["X-Replit-User-Name"] != "David-CalebCale":
    return redirect("/")
  results = request.values["id"]
  del db[results]
  return redirect("/")

app.run(host='0.0.0.0', port=81)
