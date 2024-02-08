import tkinter as tk

# window = tk.Tk()
# window.title("Hello World")
# window.geometry("300x200")

# hello = tk.Label(text="Hello World")
# hello.pack()

# button = tk.Button(text="Click me!")
# button.pack()

# #### NEW BIT ######
# canvas = tk.Canvas(
#   window, width=360,
#   height=360)  # Creates a placeholder for the image in the window.
# canvas.pack()
# image = tk.PhotoImage(file="day68/catday67.png")  # Sets the file name of the image
# image = image.subsample(2,-2) # makes the image smaller by a factor of 2
# canvas.create_image(
#   150, 1, image=image
# )  #creates image and sets the co-ordinates for it (150 is horizontal center).
# ######

# tk.mainloop()




# window = tk.Tk()
# window.title("Hello World")
# window.geometry("300x200")


# def changeImage():
#   canvas.itemconfig(
#     container,
#     image=newImage)  # itemconfig updates our canvas when this sub is called


# hello = tk.Label(text="Hello World")
# hello.pack()

# button = tk.Button(
#   text="Click me!", command=changeImage
# )  # Given the button a command to call the changeImage subroutine.
# button.pack()

# canvas = tk.Canvas(window, width=360, height=360)
# canvas.pack()
# image = tk.PhotoImage(file="day68/catday67.png")
# image = image.subsample(1, -2)

# newImage = tk.PhotoImage(file="day68/successday68.png") # filename of the replacement image assigned to newImage
# newImage = newImage.subsample(1, -2) # subsample resizes the image

# canvas.create_image(
#   150, 1, image=image
# )  #creates image and sets the co-ordinates for it (150 is horizontal center).
# ######

# container = canvas.create_image(150,1, image=image) # Assigned create image to the container variable

# tk.mainloop()



from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")

label = "Guess Who?"


def showImage():
  person = text.get("1.0", "end")
  if person.lower().strip() == "amy":
    canvas.itemconfig(container, image=Amy)
  elif person.lower().strip() == "bender":
    canvas.itemconfig(container, image=Bender)
  elif person.lower().strip() == "fry":
    canvas.itemconfig(container, image=Fry)
  elif person.lower().strip() == "leela":
    canvas.itemconfig(container, image=Leela)
  else:
    Label["text"] = "Unable to find this user"


Label = tk.Label(text=label)
Label.pack()

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(text="Find", command=showImage)
button.pack()

canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()

Amy = ImageTk.PhotoImage(Image.open("day68/Amy.png"))

Bender = ImageTk.PhotoImage(Image.open("day68/Bender.png"))
Fry = ImageTk.PhotoImage(Image.open("day68/Fry.png"))
Leela = ImageTk.PhotoImage(Image.open("day68/Leela.png"))

container = canvas.create_image(150, 1, image=Amy)

tk.mainloop()
