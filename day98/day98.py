# import schedule, time, os, smtplib
# from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
# from email.mime.text import MIMEText # Import the mime library to create text messages

# password = os.environ['mailPassword']
# username = os.environ['mailUsername']

# def sendMail():
#   email = "Don't forget to take a break!"
#   server = "smtp.gmail.com"
#   port = 587
#   s = smtplib.SMTP(host=server, port=port)
#   s.starttls()
#   s.login(username, password)
#   msg = MIMEMultipart()
#   msg["To"]= "davidcaleb1998@hotmail.com"
#   #msg["To"]= "correo@correo.com"
#   msg["From"] = username
#   msg["Subject"] = "Take a BREAK"
#   msg.attach(MIMEText(email,"plain"))

#   s.send_message(msg)
#   del msg
  
# def printMe():
#   print("⏰ Sending Reminder")
#   sendMail()

# schedule.every(1).hours.do(printMe)

# while True:
#   schedule.run_pending()
#   time.sleep(1)






import schedule
import time
import os
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = os.environ['mailPassword']
username = os.environ['mailUsername']


def sendMail(quote):
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = "davidcaleb1998@hotmail.com"
    msg["From"] = username
    msg["Subject"] = "Daily Inspiration"
    msg.attach(MIMEText(quote, "html"))
    s.send_message(msg)
    del msg
    s.quit()


quotes = []
with open("quotes.txt", "r") as file:
  for line in file:
    quotes.append(line.strip())

schedule.every(1).minutes.do(lambda: sendMail(random.choice(quotes)))

while True:
    schedule.run_pending()
    time.sleep(1)