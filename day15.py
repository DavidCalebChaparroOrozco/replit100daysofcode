# counter = 0
# while counter <10:
#   print(counter)
#   counter += 1


# counter = 0
# while counter < 100:
#   print(counter)
#   counter +=1


# exit = ""
# while exit != "yes":
#   print("🥳")
#   exit = input("Exit?: ")

exit = "no"
while exit == "no":
  animal = input("What animal sound do you want to hear?: ")
  if animal == "dog":
    print("A dog goes wof")
  elif animal == "cat":
    print("A cat goes miau")
  elif animal == "bird":
    print("A bird goes chirp")
  elif animal == "cow":
    print("A cow goes moo")
  elif animal == "horse":
    print("A horse goes neigh")
  elif animal == "pig":
    print("A pig goes oink")
  else:
    print("I don't know that animal")
  exit = input("Exit?: ")
