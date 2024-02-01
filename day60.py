import datetime

# mydate = datetime.date(year=1998, month=9, day=5)
# print(mydate)

# today = datetime.date.today()
# print(today)


# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))
# date = datetime.date(year, month, day)
# print(date)


# today = datetime.date.today()
# difference = datetime.timedelta(days=14)
# newDate = today + difference
# print(newDate)


# today = datetime.date.today()
# holiday = datetime.date(year = 2024, month = 9, day = 5)
# if holiday > today:
#   print("Coming soon")
# elif holiday < today:
#   print("Hope you enjoyed it")
# else:
#   print("HOLIDAY TIME")


today = datetime.date.today() 

print("EVENT COUNTDOWN")

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference > 0:
  print(f"{difference} days to go")
elif difference < 0:
  print(f"You missed it by {difference} days!")
else:
  print("HOLIDAY TIME!")
