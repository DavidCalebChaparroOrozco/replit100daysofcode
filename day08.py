  # name = input("Name: ")
  # if name == "Caleb" or "caleb":
  #   print("Hi Caleb")


print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name?: ")

if name =="Caleb" or name == "caleb":
  aux = input("What is the day of the week?: ")
  if aux == "monday" or aux == "Monday":
    print("It is going to be a great Monday", name)
  if aux == "tuesday" or aux == "Tuesday":
    print("What a wonderful Tuesday it is", name)
  if aux == "wednesday" or aux == "Wednesday":
    print("Happy Hump Day", name)
  if aux == "thursday" or aux == "Thursday":
    print(name,"your week is almost over!")
  if aux == "friday" or aux == "Friday":
    print(name, "It's FRIDAY!")

elif name == "David" or name== "david":
  aux = input("What is the day of the week?: ")
  if aux == "monday" or aux == "Monday":
    print("It is going to be a great Monday", name)
  if aux == "tuesday" or aux == "Tuesday":
    print("You look great in that color", name)
  if aux == "wednesday" or aux == "Wednesday":
    print("You look chipper today", name)
  if aux == "thursday" or aux == "Thursday":
    print(name,"you are doing a great job!")
  if aux == "friday" or aux == "Friday":
    print(name, "it's FRIDAY!")
else:
  print("I do not know your name, but I hope you are having a great day!")
