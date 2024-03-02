import requests, json

# result = requests.get("https://randomuser.me/api/") # ask the site for data and store it in a variable
# print(result.json()) # interpret the data in the variable as json and print it.


# user = result.json() #a dictionary containing the user's data
# # print(json.dumps(user, indent=2)) #outputs the json to the console with an indent to make it more readable.
# name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}"""  # Get the first and last names from the results dictionary and assign to a variable
# print(name)


# image = f"""{user["results"][0]["picture"]["medium"]}""" # Get the user's profile picture and assign to a variable, changing 'medium' to 'large' will make the image less pixelated
# picture = requests.get(image) # downloads the image
# file = open("image.jpg", "wb") # opens the image.jpg file for writing in binary (data of the image will be added to the repl)
# file.write(picture.content) # write the image to the file
# file.close() #closes the file
# print(image)


# if result.status_code != 200:
#   print("Error, couldn't get API")
# for person in user["results"]: #loops through each person in the results dictionary
#     name = f"""{person["name"]["first"]} {person["name"]["last"]}""" #creates a string with the name of the person
#     print(name)

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()

    for person in user["results"]:
      filename = f"""{person["name"]["first"].lower()}{person["name"]["last"].lower()}.jpg"""
      # print(filename)
      picture = requests.get(person["picture"]["medium"])
      file = open(filename, "wb")
      file.write(picture.content)
      file.close()
      print(f"Saved {filename}")
