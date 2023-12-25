# import random

# def rollDice():
#   dice = random.randint(1,6)
#   print("You rolled: ", dice)
# rollDice()

# for i in range(100):
#   rollDice()

# def myname():
#   print("My name is Caleb")
# myname()

# def countToFive():
#   for i in range(1, 6):
#     print(i)
# countToFive()

# def print_favorite_color():
#    print("My favorite color is blue.")
# print_favorite_color()


def login():
    while True:
        username = input("Enter you username: ")
        password = input("Enter your password: ")

        if username == "Caleb" and password == "ILikeTheMusic":
            print("Welcome again Caleb!")
            break
        else:
            print(
                "That is not the correct the username or password. Try again")
            continue


print("Replit Login System")
login()
