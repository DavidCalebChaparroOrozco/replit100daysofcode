# myUser = {"name": "David", "age": 25}

# myUser["name"] = "Caleb"
# print(myUser)

# print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

# myUser["age"] = 26
# print(myUser)


name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {
  "name": name,
  "dob": dob,
  "tel": tel,
  "email": email,
  "address": address
}

print(f"Name: {contact['name']}")
print(f"Date of Birth: {contact['dob']}")
print(f"Tel: {contact['tel']}")
print(f"Email: {contact['email']}")
print(f"Address: {contact['address']}")
