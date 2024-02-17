from flask import Flask

# app = Flask(__name__, static_url_path="/day76static")


# @app.route(
#     '/'
# )  # Tells the code what to do if we've gone to our web address with just a / after the URL
# def index():
#     return 'Hello from Flask!'


# @app.route('/home')  # Creates the path to the home page
# def home():  # Subroutine to create the home page
#     page = """
#   <!DOCTYPE html>
#   <html>

#   <head>
#       <meta charset="utf-8">
#       <meta name="viewport" content="width=device-width">
#       <title>replit</title>
#       <link href="style.css" rel="stylesheet" type="text/css" />
#   </head>

#   <body>
#       <img src="day76images/davidcaleb.jpg" width="30%">
#       <h1>David Caleb</h1>
#       <p class="about">The one who wants to know the northern lights more than anyone else.</p>
#       <h3>Socials</h3>
#       <ul>
#           <li> <a href="https://www.linkedin.com/in/david-caleb-chaparro-orozco-32a128192/">LinkedIn </a> </li>
#           <li> <a href="#"> Email ( davidcaleb1998@hotmail.com ) </a> </li>
#       </ul>
#   </body>

#   </html>
#   """
#     # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
#     return page  # returns the contents of the page variable


# app.run(
#     host='0.0.0.0', port=81
# )  # This line should ALWAYS come last. It's the line that turns on the Flask server.


from flask import Flask

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
  page = f"""
    <html>
      <body>
        <p>> <a href ="/portfolio">Go portfolio </a></p>
        <p>> <a href ="/linktree">Go linktree </a></p>
      </body>
    </html>
    """
  return page

@app.route("/portfolio")
def portfolio():
    page = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Portfolio</title>
    <link href="day76/static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <img src="../static/images/davidcaleb.png" width="50%">
    <h1>David Caleb</h1>
    <p class="about">The one who wants to know the northern lights more than anyone else.</p>
    <h3>Socials</h3>
    <ul>
        <li> <a href="https://www.linkedin.com/in/david-caleb-chaparro-orozco-32a128192/">LinkedIn </a> </li>
        <li> <a href="#"> Email ( davidcaleb1998@hotmail.com ) </a> </li>
    </ul>
</body>

</html>
"""
    return page


@app.route("/linktree")
def linktree():
    page = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Caleb's World of Adventure</title>
    <link href="day76/static/css/linktree.css" rel="stylesheet" type="text/css"/>
</head>

<body>
    <h1>Caleb's World of Adventure</h1>
    <h2>Welcome to our website!</h2>
    <p>We all know that throughout history some of the greatest have been those who, let's the epicness speak for
        itself, have witnessed something extraordinary. But that's not the only thing that has captured our hearts.</p>

    <h2>Gallery of Adventure</h2>
    <p>Here are some of the places we've been and things we've experienced on our journeys:</p>
    <img src="../static/images/norway_aurora_forecast.png" width="50%">
    <p>Norway is one of the best places to experience the Northern Lights.</p>

    <ul>
        <li>Beautiful scenery</li>
        <li>Nice place to visit</li>
        <li>Nice people</li>
    </ul>
    <p> <a href="https://www.visitnorway.com/things-to-do/nature-attractions/northern-lights/">Know about the Northern
            Lights. </N></a></p>
</body>

</html>
"""
    return page

app.run(host='0.0.0.0', port = 81)
