from flask import Flask, request

app = Flask(__name__)


# @app.route('/', methods=["GET"])
# def index():
#   return request.args


# @app.route("/", methods=["GET"])
# def index():
#     get = request.args
#     if get["name"].lower() == "caleb":
#         return "Hello Caleb!"
#     return "No data!" 

# app.run(host='0.0.0.0', port=81)

# http://127.0.0.1:81/?=caleb
# http://127.0.0.1:81/?name=caleb&age=25

@app.route("/language", methods = ["GET"])
def lang():
    data = request.args
    if data == {}:
        return "Nothing here"
    if data["lang"]=="eng":
        return "Hello, and Welcome to website!"
    elif data["lang"]=="esp":
        return "Hola y bienvenido a este sitio web"
    else:
        return "Nothing to see here"
    
@app.route("/")
def index():
    return "Hello World!"

app.run(host="0.0.0.0", port=81)

# http://127.0.0.1:81/language?lang=eng
# http://127.0.0.1:81/language?lang=esp
# http://127.0.0.1:81/language?lang=aaa
