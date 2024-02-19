from flask import Flask, redirect

# app = Flask(__name__)

# @app.route('/')
# def index():
#     myName = "Caleb"
#     title = "Day 77"
#     text = "As you probably have figured out by now, your flask files get pretty big pretty quickly. Let's use Flask to slim things down a bit."
#     image = "davidcaleb.jpg"
#     link = "https://www.linkedin.com/in/david-caleb-chaparro-orozco-32a128192/"
    
#     page = ""
#     with open("template/index.html", "r") as file:
#         page = file.read()
    
#     page = page.replace("{name}", myName)
#     page = page.replace("{title}", title)
#     page = page.replace("{text}", text)
#     page = page.replace("{image}", image)
#     page = page.replace("{link}", link)
    
#     return page


# @app.route('/home')
# def home():
#   page = """
# <html>
# <head>
#     <title>Caleb's World of Adventure</title>
#     <link href="/static/css/portfolio.css" rel="stylesheet" type="text/css" />
# </head>

# <body>
#     <h1>Caleb's World of Adventure</h1>
#     <h2>Welcome to our website!</h2>
#     <p>We all know that throughout history some of the greatest have been those who, let's the epicness speak for
#         itself, have witnessed something extraordinary. But that's not the only thing that has captured our hearts.</p>

#     <h2>Gallery of Adventure</h2>
#     <p>Here are some of the places we've been and things we've experienced on our journeys:</p>
#     <img src="static/images/norway_aurora_forecast.png" width="50%">
#     <p>Norway is one of the best places to experience the Northern Lights.</p>

#     <ul>
#         <li>Beautiful scenery</li>
#         <li>Nice place to visit</li>
#         <li>Nice people</li>
#     </ul>
#     <p> <a href="https://www.visitnorway.com/things-to-do/nature-attractions/northern-lights/">Know about the Northern
#             Lights. </N></a></p>
# </body>
# </html>
# """
#   return page

# @app.route('/77')
# def seventySeven():
#    return redirect("https://www.youtube.com/watch?v=3mMVcCMO_Ng")


# app.run(host='0.0.0.0', port=81)

app = Flask(__name__)

@app.route("/")
def index():
    title = "Hello World, here Caleb!"
    date = "February 18th 2024"
    text = "Here is my first blog entry with beloved cats."
    image = "cats.jpg"
    page = ""

    with open("template/blog.html", "r") as file:
        page = file.read()

    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    page = page.replace("{image}",image)
    return page

app.run(host="0.0.0.0",port=81)