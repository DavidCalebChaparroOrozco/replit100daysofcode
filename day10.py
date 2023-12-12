# adding = 4 + 3
# print(adding)

# subtraction = 8 - 9
# print(subtraction)

# multiplication = 4 * 32
# print(multiplication)

# division = 50 / 5
# print(division)

# # a number raised to the power of some number
# # in this example we raise 5 to the power of 2
# squared = 5**2
# print(squared)

# # remainder of a division
# modulo = 15 % 4
# print(modulo)

# # whole number division
# divisor = 15 // 2
# print(divisor)


# # 👉 Solve the following problems with my code
# # Your goal is to print the solution of all 3 calculations to the screen.

# # multiplication
# multiplication = 3.4 * 6.8
# print(multiplication)

# # division
# division = 2467 / 4673
# print(division)

# #raise 10 to the power of 2
# squared = 10**2
# print(squared)

# # print the remainder when 343 is divided by 4
# remainder = 343//100
# print(remainder)


myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("How much tip are you going to leave?: "))
bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_bill = round(bill_per_person, 2)
print("You all owe", final_bill)
