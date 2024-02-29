# from flask import Flask, request, redirect

# app = Flask(__name__)

# @app.route('/')
# def index():
#   if request.headers["X-Replit-User-Name"]:
#     return redirect("/hi")
#   page = ""
#   file = open("page.html", "r")
#   page = file.read()
#   file.close()
#   return page


# @app.route("/hi")
# def hi():
#   if not request.headers["X-Replit-User-Name"]:
#     return redirect("/")
#   page = ""
#   page += f"""<h1>{request.headers["X-Replit-User-Name"]}</h1>"""
#   page += f"""<img src="{request.headers["X-Replit-User-Profile-Image"]}" width="200">"""
#   return page
# app.run(host='0.0.0.0', port=81)





from flask import Flask, request, redirect
from replit import db
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  userid = request.headers['X-Replit-User-Name']
  page = ""
  f = open("index.html", "r")
  # f = open("template/index.html", "r")
  page = f.read()
  f.close()
  keys = sorted(db.keys(), reverse= True)
  for key in keys:
    page += "<hr>"
    page += f"<h1>{db[key]['title']}</h1>"
    page += f"<p>{db[key]['content']}<p>"
    page += f"<p>posted on {db[key]['ara']}<p>"
  if userid == 'David-CalebCale':
    return redirect('/content')
  else: 
    page += "<p>ONLY ALLOWED TO READ MA BLOG</p>"
    return page

@app.route('/content')
def content():
  page = ""
  f = open("content.html", "r")
  # f = open("template/content.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{user}", request.headers['X-Replit-User-Name'])
  keys = sorted(db.keys(), reverse= True)
  for key in keys:
    page += "<hr>"
    page += f"<h1>{db[key]['title']}</h1>"
    page += f"<p>{db[key]['content']}<p>"
    page += f"<p>posted on {db[key]['ara']}<p>"
  return page


@app.route('/logged', methods = ["POST"])
def data():
  now = datetime.datetime.now()
  form = request.form
  db[f"dates_{now}"] = {'ara': f'{now}', 'title': f'{form["title"]}', 'content': f'{form["content"]}'}  
  return redirect('/content')

@app.route('/naughty')
def naughty():
  return "You are not allowed to see this page"

app.run(host='0.0.0.0', port=81)