# for counter in range(10):
#     print(counter)


# total = 0
# for number in range(100):
#   total += number
#   print(total)


# for days in range(7):
#   print("Day", days)


# total = 10
# for counter in range(100):
#   total += 10
#   print(total)


loan = 10000
rate = 0.05

for i in range(10):
  loan+=(loan*rate)
  print("Year", i+1, "is: ", round(loan,2))
