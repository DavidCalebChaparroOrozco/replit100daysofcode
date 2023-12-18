# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")


# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
# print("Bye!")


# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")

print("Welcome to Name the Song Lyric")
print("Figure out the missing word as quickly as you can!")

counter = 1
while True:
  lyrics = input(
    """
    
    I ____ I'll be alright
    But I'm not tonight 
    I'll be lying awake
    
    """) #know
  if lyrics == "know" or lyrics == "Know":
    print("You got it!")
  else:
    print("No, try again!")
    counter += 1
  if lyrics == "know" or lyrics == "Know":
    break
print("Ty for playing")

print("You got the correct lyrics in", counter, "attemp(s)")
