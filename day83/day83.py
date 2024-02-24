from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    page = ""
    return page

@app.route("/hello", methods = ["GET"])
def hello():
    data = request.args
    template = "default"
    if data != {}:
        template = data["template"]
    title = "Hello World, here Caleb!"
    date = "February 24th 2024"
    text = "Here is my first blog entry with beloved cats"
    image = "../images/cats.jpg"
    page = ""
    with open("template/index.html", "r") as file:
        page = file.read()

    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    page = page.replace("{image}",image)
    page = page.replace("{template}", template)
    return page


@app.route("/bye", methods = ["GET"])
def bye():
    data = request.args
    template = "default"
    if data != {}:
        template = data["template"]
    title = "Bye World!"
    date = "February 25th 2024"
    text = "Here is my last blog in Norway"
    image = "../images/norway_aurora_forecast.png"
    page = ""
    with open("template/index.html", "r") as file:
        page = file.read()

    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    page = page.replace("{image}",image)
    page = page.replace("{template}", template)
    return page

app.run(host="0.0.0.0",port=81)

# http://127.0.0.1:81/hello
# http://127.0.0.1:81/hello?template=style
# http://127.0.0.1:81/hello?template=default
# http://127.0.0.1:81/bye
# http://127.0.0.1:81/bye?template=style
# http://127.0.0.1:81/bye?template=default