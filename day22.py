import random

# mynumber = random.randint(1, 100)
# print(mynumber)

# for i in range(10):
#   mynumber = random.randint(1, 100)
#   print(mynumber)


# myNumber = random.randint(1, 10)
# for i in range(10):
#   print(myNumber)


print("Totally Random One-Million-to-One")

attempt = 1
answer = random.randint(1,1000000)

condition = True
while True:
    user = int(input("Pick a number between 1 and 1,000,000: "))
    if user < 0:
        print("You can't pick a negative number.")
    if user < answer:
        print("Your number is too low. Try Again.")
        attempt += 1
        continue
    elif user > answer:
        print("Your number is too high. Try Again")
        attempt += 1
        continue
    elif user == answer:
        print("You are a winner")
        break
    else:
        print("Something went wrong")
    print("It took you "+ str(attempt) + "attempts! Good Job!")
