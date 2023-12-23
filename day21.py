print("Math Game")

fact = int(input("Name your multiples: "))

counter = 0
for i in range(1,11):
  correct = i*fact
  print(f"{i} x {fact}")
  answer = int(input(": "))
  if answer == correct:
    print("You got it")
    counter += 1
  else:
    print("That's not correct. It should have been", correct)

if counter == 10:
  print("Perfect score!")
else:
  print("You got", counter, "out of 10")
