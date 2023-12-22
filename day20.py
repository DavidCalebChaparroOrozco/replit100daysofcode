# for i in range(100, 110):
#   print(i)

# for i in range(1, 7):
#   print("Day", i)


# print("Thirteen Times Table")
# for i in range(1, 13):
#   print(i, "x 13 =", i * 13)


# for i in range (0, 1000000, 25):
#   print(i)


# for i in range(10, -1, -1):
#   print(i)

print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")

number_1 = int(input("What number do you want to start with?: "))
number_2 = int(input("What number do you want to end with?: "))
number_3 = int(input("How many should I add each time?: "))

for i in range(number_1, number_2,number_3):
  print(i)
