from flask import Flask, request, redirect, session  # extra session import
import os

app = Flask(__name__, static_url_path='/static')

app.secret_key = os.getenv('sessionKey') or os.urandom(24) # new line to include the key, inside [''] is the key you created
print(app.secret_key)

users = {}
users["Caleb"] = {"name": "Caleb", "password": "caleb1"} 
users["David"] = {"name": "David", "password": "david1"}
blogs = {}


def getBlogs():
  content = ""
  sorted_entries = sorted(blogs.values(), key=lambda x: x['date'], reverse=True)  
  for entry in sorted_entries:
    content += f"<h2>{entry['title']}</h2>"
    content += f"<h3>{entry['date']}</h3>"
    content += f"<p>{entry['body']}</p>"
    content += "<hr>"
  return content


@app.route('/')
def index():
  if session.get("user"):
    return redirect("/edit")
  return redirect("/loginForm")

@app.route('/loginForm')
def loginForm():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  with open("template/login.html",'r') as file:
    page = file.read()
  page = page.replace("{content}", getBlogs())
  return page

@app.route('/login', methods=["POST"])
def login():
  if session.get("user"):
    return redirect("/edit")
  form = request.form
  if form["username"] in users:
    if form["password"] == users[form["username"]]["password"]:
      session["user"] = True
      return redirect("/edit")
  else:
    return redirect("/loginForm")

@app.route('/edit')
def edit():
  if not session.get("user"):
    return redirect("/")
  page = ""
  with open("template/edit.html",'r') as file:
    page = file.read()
  page = page.replace("{content}",getBlogs())
  return page



@app.route('/add', methods=["POST"])
def add():
  form = request.form
  entry_id =len(blogs) + 1
  entry = {
      "title": form["title"],
      "date": form["date"],
      "body": form["body"]
      }
  # users[form["title"]] = entry
  blogs[entry_id] = entry
  return redirect("/edit")

@app.route('/logout')
def logout():
  session.clear()
  return redirect("/")

app.run(host='0.0.0.0', port = 81)