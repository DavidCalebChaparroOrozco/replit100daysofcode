# my1DList = ["Johnny", 21, "Mac"]
# print(my1DList)
# # ['Johnny', 21, 'Mac']

# my2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]
# print(my2DList)
# # [['Johnny', 21, 'Mac'], ['Sian', 19, 'PC'], ['Gethin', 17, 'PC']]

# my2DList = [["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"]]
# print(my2DList[0][0])
# # Johnny

# print(my2DList[1][2])
# # PC

# my2DList[1][2] = "Linux"
# print(my2DList[1])
# # ['Sian', 19, 'Linux']


# # my2DList = [ ["Johnny", 21, "Mac"],
# #              ["Sian", 19, "PC"],
# #              ["Gethin", 17, "PC"] ]
# # print(my2DList[0][2])


# # my2DList =  [ ["Johnny", 21, "Mac"],
# #              ["Sian", 19, "PC"],
# #              ["Gethin", 17, "PC"] ]
# # print(my2DList[0][1])


import random
bingo = []
def ran():
  number = random.randint(1, 90)
  return number
def prettyPrint():
  for row in bingo:
    print(row)
numbers = []
for i in range(8):
  numbers.append(ran())
numbers.sort()
bingo = [[numbers[0], numbers[1],
          numbers[2]], [numbers[3], "BINGO", numbers[4]],
         [numbers[5], numbers[6], numbers[7]]]
prettyPrint()
