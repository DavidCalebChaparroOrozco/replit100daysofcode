# myString = "Hello World, here Caleb"
# print(myString[0]) # H

# print(myString[6:11]) 
# # H
# # World

# print(myString[:11])
# # Hello World

# print(myString[12:])
# # here Caleb

# print(myString[0:6:2])
# # Hlo

# print(myString[::3])
# # HlWl rCe

# print(myString[::-1])
# # belaC ereh ,dlroW olleH

# print(myString.split())
# # ['Hello', 'World,', 'here', 'Caleb']

# print(myString[0:5])
# # Hello

# print(myString[:4:1])
# # Hell

# print(myString[0:11:1])
# # Hello World


print("Star Wars NAME GENERATOR")
name = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ").split()
first = name[0].strip()
last = name[1].strip()
maiden = name[2].strip()
city = name[3].strip()
full_name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"
print(f"Your Star Wars name is {full_name}")
