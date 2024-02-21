from flask import Flask, request

app = Flask(__name__)


# @app.route("/process", methods=["POST"])
# def process():
#     page = ""
#     form = request.form

#     if form["Foods"] == "Pizza":
#         page += f"We like the same, {form['username']}"
#     else:
#         page += f"Mmmm sounds delicious but I prefer pizza, {form['username']}"
#     return page


# @app.route("/")
# def index():
#     page = """
# <!DOCTYPE html>
# <html>

# <head>
#     <meta charset="utf-8" />
#     <meta name="viewport" content="width=device-width" />
#     <title>replit</title>
#     <link href="style.css" rel="stylesheet" type="text/css" />
# </head>

# <body>
#     <form method="post" action="/process">
#         <p>Name: <input type="text" name="username" required></p>
#         <p>Email: <input type="Email" name="email" /></p>
#         <p><input type="hidden" name="userID" value="232" /></p>
#         <p>
#             Fave Food:
#             <select name="Foods">
#                 <option value="Hamburger">Hamburger</option>
#                 <option value="Pizza">Pizza</option>
#                 <option value="Hot Dog">Hot Dog</option>
#             </select>
#         </p>
#         <button type="submit">Save Data</button>
#     </form>
# </body>

# </html> 
# """
#     return page

# app.run(host='0.0.0.0',port=81)

logins = {}
logins["caleb"] = {"email": "c@c.com", "password" : "caleb1"}
logins["david"] = {"email": "d@d.com", "password" : "david1"}
logins["manuela"] = {"email": "m@m.com", "password" : "manu1"}

@app.route("/login", methods = ["POST"])
def login():
    form = request.form
    isThere = False
    details = {}
    try:
        details = logins[form["username"]]
        isThere = True
    except:
        return "Username, Email or Password incorrect"
    if form["email"] == details["email"] and form["password"] == details["password"]:
        return "You are logged in"
    else:
        return "Username, Email or Password incorrect"


@app.route("/")
def index():
    page = """
<body>
    <form method="post" action="/login">
        <p>Name: <input type="text" name="username" required></p>
        <p>Email: <input type="Email" name="email" /></p>
        <p>Password: <input type="password" name="password"></p>
        <button type="submit">Save Data</button>
    </form>
</body>
"""
    return page

app.run(host="0.0.0.0", port =81)

