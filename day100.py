import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from replit import db

def addToDB():
  #link = input("Link: ")
  link = "https://www.wexphotovideo.com/bowens-lpl1-50-led-panel-1754160/"
  #price = float(input("Price: "))
  #db[time.time()] = {"link": link, "price": None, "level": price}

def emailMe(level, price, link):
  password = os.environ['mailPassword']
  username = os.environ['mailUsername']
  host = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host=host, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "Product is Cheaper!"
  text = f"""<p><a href='{link}'>This item</a> is now ${price} which is below your purchase level of {level}</p>"""
  msg.attach(MIMEText(text, 'html'))
  s.send_message(msg)
  del msg
  
def update():
  keys = db.keys()
  for key in keys:
    url = db[key]["link"]
    price = db[key]["price"]
    level = db[key]["level"]
  
    try:
      response = requests.get(url)
      response.raise_for_status()  # Check for HTTP errors
  
      html = response.text
      soup = BeautifulSoup(html, "html.parser")
  
      # price wex-red
      myPrice = soup.find_all("span", {"class": "price"})
  
      if myPrice:  # Check if myPrice is not empty
        thisPrice = float(myPrice[0].text[1:].replace(",", ""))
  
        if thisPrice != price:
          db[key]["price"] = thisPrice
          if thisPrice <= level:
            print("Cheaper")
            emailMe(level, price, url)
  
    except requests.RequestException as e:
      print(f"Error fetching data from {url}: {e}")

schedule.every(1).day.do(update)

while True:
  schedule.run_pending()
  time.sleep(1)

#db[time.time()] = {"link": "https://www.wexphotovideo.com/bowens-lpl1-50-led-panel-1754160/", "price": None, "level": 120}

#https://www.wexphotovideo.com/sony-a7-iv-digital-camera-body-3020039/

#https://www.wexphotovideo.com/bowens-lpl1-50-led-panel-1754160/
