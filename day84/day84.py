from flask import Flask, request, redirect
# from replit import db

app = Flask(__name__, static_url_path="/static")

# # db["caleb"] = {"password": "caleb1"}
# # db["david"] = {"password": "david1"}

# users = {}
# users["Caleb"] = {"password": "caleb1"}
# users["david"] = {"password": "david1"}

# @app.route("/login", methods=["POST"])
# def login():
#     form = request.form

#     try:
#       if users[request.form["username"]]["password"] == request.form["password"]:
# #   if db[request.form["username"]]["password"] == request.form["password"]:
#         return redirect("/yes")
#       else:
#             return redirect("/no")
#     except KeyError:
#         return redirect("/no")

# # Login checking code - uses POST because it's dealing with usernames & passwords so we want encryption

# # If the user details are correct, they get a lovely success gif, if not, they get a 'nope' gif.

# # Try except used to load the 'nope' in case there's an error.

# @app.route("/yes")
# def yes():
#   page = """<img src="static/images/yup.gif" height="100">"""
#   file = open("template/change.html", "r")
#   page += file.read()
#   file.close()
#   return page

# @app.route("/no")
# def no():
#   return """<img src="static/images/nerdy.gif" height="100">"""

# # The two methods above load the relevant gif depending on the result of the '/login' method

# @app.route("/changePass", methods=["POST"])
# def change():
#   form = request.form
# #   db[request.form["username"]] ["password"]= request.form["newPassword"]
#   users[request.form["username"]] ["password"]= request.form["newPassword"]
#   return f"""Password changed to {request.form['newPassword']}"""


# @app.route("/")
# def index():
#     page = ""
#     with open("template/login.html", "r") as file:
#         page = file.read()
#     return page

# app.run(host="0.0.0.0", port=81)








users = {}
users["Caleb"] = {"name": "Caleb", "password": "caleb1"} 
users["David"] = {"name": "David", "password": "david1"}

@app.route('/signup', methods= ["POST"])
def createUser():
    form = request.form
    if form["username"] not in users:
        users[form["username"]] = {"name": form["name"], "password": form["password"]}
        return redirect("/login")
    else:
        return redirect("/signup")

@app.route("/doLogin", methods=["POST"])
def doLogin():
    form = request.form
    if form["username"] in users:
        if form["password"] == users[form["username"]]["password"]:
            return f"Hello {users[form['username']]['name']}"
        else:
            return "Invalid username or password"  # Muestra un mensaje de error
    else:
        return "Invalid username or password"  # Muestra un mensaje de error

        
@app.route('/signup', methods = ["GET"])
def signup():
    page = ""
    with open("template/signup.html", "r") as file:
        page = file.read()
    return page

@app.route('/login', methods = ["GET"])
def login():
    page = ""
    with open("template/login.html", "r") as file:
        page = file.read()
    return page


@app.route("/")
def index():
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