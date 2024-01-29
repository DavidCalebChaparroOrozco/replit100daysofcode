# def reverse(value):
#   if value <= 0:
#     print("Done")
#     return
#   else:
#     for i in range(value):
#       print("💯", end="")
#     print()
#     reverse(value - 2)
# reverse(10)


def factorial(number):
  if number ==1:
    return 1
  else:
    return number * factorial(number-1)

print(factorial(3))
