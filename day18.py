number = 1998
attempt = 1
while True:
  user = int(input("Pick a number between 1 and 10,000,000: "))
  if user < 0:
    print("You can't pick a negative number.")
    exit()
  if user < number:
    print("Your number is too low. Try Again.")
    attempt += 1
    continue
  elif user > number:
    print("Your number is too high. Try Again.")
    attempt += 1
    continue
  elif user == number:
    print("You are a winner")
    break
  else:
    print("Something went wrong.")
print("It took you "+ str(attempt) + " attempts! Good job!")
