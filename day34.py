import os, time
# listEmail = []

# def prettyPrint():
#   print("List Email: ")
#   print()
#   counter = 1
# #   for email in listEmail:
# #     print(f"{counter}: {email}")
#   for index in range(len(listEmail)):
#     print(f"{index}: {listEmail[index]}")
#     counter += 1
# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n: ")
#   if menu == "1":
#     email = input("Email : ")
#     listEmail.append(email)
#   elif menu == "2":
#     email = input("Email : ")
#     if email in listEmail:
#       listEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)


# listOfEmail = []

# def prettyPrint():
#   os.system("clear") 
#   print("listofEmail") 
#   print()
#   counter= 1
#   for index in range(len(listOfEmail)): 
#     print(f"{index}: {listOfEmail[index]}")
#     counter += 1 
#   time.sleep(1)
# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint() 
#   time.sleep(1)
#   os.system("clear")


# listOfFood = []

# def prettyPrint():
#   print("listofFood") 
#   print()
#   counter = 1
#   for order in listOfFood: 
#     print(f"{counter}: {order}") 
#     counter += 1 
#   time.sleep(1)
# while True:
#   print("Yummy Food Restaurant")
#   menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
#   if menu == "1":
#     order = input("order : ")
#     listOfFood.append(order)
#   elif menu =="2":
#     order = input ("delete order: ")
#     if order in listOfFood:
#       listOfFood.remove(order)
#   elif menu == "3": 
#     prettyPrint() 
#   time.sleep(1)


listEmail = []
def prettyPrint():
    print("List Email")
    print()
    counter = 1
    for email in listEmail:
        print(f"{counter}: {email}")
        counter += 1
    time.sleep(1)

def spam(max):
    for i in range(0, max):
        if i < len(listEmail):
            print(f"""Email {i+1}

Dear Team {listEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We 
insist you do it right away. If you don't we will pass on your email address to every spammer we've
ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We 
might just do that anyway

Love and Hugs,
David Caleb Chaparro Orozco""")
    time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listEmail:
      listEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
     spam(10)
  time.sleep(1)
