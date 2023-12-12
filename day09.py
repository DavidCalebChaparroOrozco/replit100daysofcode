# Score = input("Your score: ")
# if Score > 100000:
#   print("Winner!")
# else:
#   print("Try again 😭")



# Score = int(input("Your score: "))
# if Score > 100000:
#   print("Winner!")
# else:
#   print("Try again 😭")



# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")



# myPi = float(input("What is Pi to 3dp? "))
# if myPi == 3.142:
#   print("Exactly!")
# else:
#   print("Try again 😭")



# myPi = float(input("What is Pi to 3dp?"))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭")



# score = int(input("What was your score on the test?: "))
# if score >= 80:
#   print("Not too shabby")
# elif score >= "70":
#   print("Acceptable.")
# else:
#   print("Dude, you need to study more!")



# age = int(input("What year were you born?: "))
# if age <= 1946:
#   print("You are a Traditionalist")
# elif age >= 1947 and age <= 1964:
#   print("You are a Baby Boomers")
# elif age >= 1965 and age <= 1981:
#   print("You are a Generation X")
# elif age >= 1982 and age <= 1995:
#   print("You are a Millenial")
# elif age >= 1996 and age <= 2015:
#   print("You are a Generation Z")
# else:
#   print("Try again")



GENERATIONS = {
  "Traditionalist": (1946, None),
  "Baby Boomers": (1947, 1964),
  "Generation X": (1965, 1981),
  "Millenials": (1982, 1995),
  "Generation Z": (1996, 2015),
}

try:
  age_birth = int(input("What year were you born?: "))
  for generation, (start_year, end_year) in GENERATIONS.items():
      if start_year is None or age_birth >= start_year:
          if end_year is None or age_birth <= end_year:
              print(f"You are a {generation}")
              break
  else:
      print("Try again. Please enter a valid year.")
except ValueError:
  print("Invalid input. Please enter a valid year.")
