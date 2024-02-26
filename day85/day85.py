from flask import Flask, request, redirect, session  # extra session import
import os

app = Flask(__name__)

# # app.secret_key = os.environ['sessionKey']  
app.secret_key = os.getenv('sessionKey') or os.urandom(24) # new line to include the key, inside [''] is the key you created
print(app.secret_key)
# @app.route('/')
# def index():
#   page = ""
#   myName = ""
#   if session.get("myName"):
#     myName = session["myName"]
#   page += f"<h1>{myName}</h1>"
#   # file = open("index.html", "r")
#   file = open("template/index.html", "r")
#   page += file.read()
#   return page


# @app.route("/setName", methods=["POST"])
# def setName():
#     session["myName"] = request.form["name"]
#     return redirect("/")


# @app.route("/reset")
# def reset():
#     session.clear()
#     return redirect("/")


# app.run(host='0.0.0.0', port=81)


users = {}
users["Caleb"] = {"name": "Caleb", "password": "caleb1"} 
users["David"] = {"name": "David", "password": "david1"}

@app.route('/signup', methods= ["POST"])
def createUser():
  if session.get("loggedIn"):
    return redirect("/welcome")
  form = request.form
  if form["username"] not in users:
    users[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route("/doLogin", methods=["POST"])
def doLogin():
  if session.get("loggedIn"):
    return redirect("/welcome")
  form = request.form
  if form["username"] in users:
    if form["password"] == users[form["username"]]["password"]:
      session["loggedIn"] = form["username"]
      # return f"Hello {users[form['username']]['name']}"
      return redirect("/welcome")
    else:
      # return redirect("/welcome")
      return redirect("/login")
  else:
    return redirect("/login")
    

@app.route('/welcome')
def welcome():
  page = f"""
  <h1> Hi there {users[session["loggedIn"]]["name"]}</h1>
  <button type="button" onClick="location.href='/logout'">Log out </button>
  """
  return page

@app.route('/logout')
def logout():
  session.clear()
  return redirect("/")

        
@app.route('/signup', methods = ["GET"])
def signup():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page = ""
  with open("template/signup.html", "r") as file:
    page = file.read()
  return page

@app.route('/login', methods = ["GET"])
def login():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page = ""
  with open("template/login.html", "r") as file:
    page = file.read()
  return page


@app.route("/")
def index():
  if session.get("loggedIn"):
    return redirect("/welcome")
  page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log In</title>
</head>
<body>
    <p><a href="/signup">Sign Up</a></p>
    <p><a href="/login">Log In</a></p>
</body>
</html>
"""
  return page
    
app.run(host="0.0.0.0", port=81)