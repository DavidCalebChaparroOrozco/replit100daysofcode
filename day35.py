import os, time

print("To Do List Manager: ")
To_DoList = []


def printList():
  for item in To_DoList:
    print(item)


while True:
  menu = input("Do you want to view, add, edit, or remove your To Do list?: ")
  if menu == "add":
    item = input("What do you want to add?: ")
    To_DoList.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in To_DoList:
      To_DoList.remove(item)
  elif menu == "view":
    printList()
  elif menu == "edit":
    item_index = int(input("Enter the index of the item you want to edit: "))
    if 0 <= item_index < len(To_DoList):
      new_item = input("Enter the new item: ")
      To_DoList[item_index] = new_item
      print("Item edited successfully!")
  elif menu == "delete":
    To_DoList = []
  time.sleep(1)
  os.system("clear")
