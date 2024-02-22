from flask import Flask, request

app = Flask(__name__)

@app.route("/robot", methods=["POST"])
def robot():
    form = request.form
    if form['metal'] == "yes":
        return "You're a robot!"
    elif "error" in form["infinity"].lower():
        return "You're a robot!"
    elif form["food"] == "synthetic oil":
        return "You're a robot!"
    else:
        return "You're a human"


@app.route("/")
def index():
    page = ""
    file = open("template/index.html","r")
    page = file.read()
    file.close()
    return page

app.run(host='0.0.0.0', port = 81)