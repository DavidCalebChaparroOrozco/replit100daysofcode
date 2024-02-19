from flask import Flask

app = Flask(__name__)

myReflections = {}
myReflections["77"] = {"link": "#", "Reflection": "Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css 😿"}
# myReflections["77"] = {"link": "https://github.com/DavidCalebChaparroOrozco/replit100daysofcode/tree/main/day77", "Reflection": "Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css 😿"}
myReflections["78"] = {"link": "#", "Reflection": "Oh. Easy. Done. Boom"}
# myReflections["78"] = {"link": "https://github.com/DavidCalebChaparroOrozco/replit100daysofcode/tree/main/day76", "Reflection": "Oh. Easy. Done. Boom"}


@app.route('/')
def home():
    return """See <a href='/77'>here</a> or <a href='/78'>here</a>. <link href="/static/css/style.css" rel="stylesheet" type="text/css" />"""


@app.route('/<pageNumber>')
def index(pageNumber):
    global myReflections
    if pageNumber in myReflections:
        page = ""
        with open("template/index.html","r") as file:
            page = file.read()

        page = page.replace("{day}", pageNumber)
        page = page.replace("{date}", myReflections[pageNumber]["link"])
        page = page.replace("{Reflection}", myReflections[pageNumber]["Reflection"])
        return page
    else:
        return "Page not found"

app.run(host='0.0.0.0', port=81)