# myAgenda = []
# def printList():
#   for item in myAgenda:
#     print(item)
# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = input("What do you want to remove?: ")
#     myAgenda.remove(item)
#     if item in myAgenda:
#       myAgenda.remove(item)
#   else:
#     print(f"{item} was not in the list")
#   printList()


# myPartyList = []
# def printList():
#   print() 
#   for item in myPartyList:
#     print(item)
#   print() 
# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("Who should I add to the party list?: ")
#     myPartyList.append(item)
#   elif menu == "remove":
#     item = input("Who should I remove from the party list?: ")
#     if item in myPartyList:
#       myPartyList.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()

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
