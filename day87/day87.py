from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ['secretKey']

#userId = request.headers["X-Replit-User-Name"]
#print(userId)

def getBlogs():
  entry = ""
  file = open("template/entry.html", "r")
# "template/entry.html"
  entry = file.read()
  file.close()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content

@app.route("/")
def index():
  userId = request.headers['X-Replit-User-Name']
  #print(userId)
  if userId == "David-CalebCale":
  #if session.get("user"):
    return redirect("/edit")
  page = ""
  file = open("template/blog.html", "r")
# "template/blog.html"
  page = file.read()
  file.close()
  page = page.replace("{content}", getBlogs())
  return page

@app.route("/loginForm")
def loginForm():
  userId = request.headers['X-Replit-User-Name']
  #print(userId)
  if userId == "David-CalebCale":
  #if session.get("user"):
    return redirect("/edit")
  page = ""
  file = open("template/login.html", "r")
  #template/login.html
  page= file.read()
  file.close()
  return page

@app.route("/login", methods=["POST"])
def login():
  userId = request.headers['X-Replit-User-Name']
  #print(userId)
  if userId == "David-CalebCale":
  #if session.get("user"):
    return redirect("/edit")
  form = request.form
  if form["username"] == db["user"]["username"] and form["password"] == db["user"]["password"]:
    session["user"] = True
    return redirect("/edit")
  else:
    return redirect("/loginForm")

@app.route("/edit")
def edit():
  userId = request.headers['X-Replit-User-Name']
  #print(userId)
  if userId == "David-CalebCale":
  #if session.get("user"):
    return redirect("/")
  page = ""
  file = open("template/edit.html", "r")
  # template/edit.html
  page = file.read()
  page = page.replace("{content}", getBlogs())
  file.close()
  return page

@app.route("/add", methods=["POST"])
def add():
  userId = request.headers['X-Replit-User-Name']
  #print(userId)
  if userId != "David-CalebCale":
  #if session.get("user"):
    return redirect("/")
  form = request.form
  entry = {
    "title": form["title"],
    "date": form["date"],
    "body": form["body"]
  }
  db[form["date"]] = entry
  return redirect("/edit")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")

app.run(host="0.0.0.0", port=81)