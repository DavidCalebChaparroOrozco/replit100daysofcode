import tkinter as tk

# window = tk.Tk()
# window.title("Hello World!") 
# window.geometry("300x200") 

# labelOn = True

# def hideLabel():
#   global labelOn
#   if labelOn:
#     root.pack_forget() # hides the label
#     labelOn = False
#   else:
#     button.pack_forget() # hides the button
#     root.pack() # shows the label
#     button.pack() # reloads the button
#     labelOn = True

# root = tk.Label(text = "Hello World") 
# root.pack() 

# button = tk.Button(text = "Click me!", command=hideLabel) # calls the hideLabel function
# button.pack()

# tk.mainloop()


# import tkinter as tk

# window = tk.Tk()
# window.title("Hello World")
# window.geometry("300x200")


# def changeImage():
#   canvas.itemconfig(container, image=newImage)


# def hideImage():
#   canvas.pack_forget()


# root = tk.Label(text="Hello World")
# root.pack()

# button = tk.Button(text="Click me!", command=changeImage)
# button.pack()

# button2 = tk.Button(text="Hide Image", command=hideImage)
# button2.pack()

# canvas = tk.Canvas(window, width=360, height=360)
# canvas.pack()
# image = tk.PhotoImage(file="day68/catday68.png")
# image = image.subsample(1, -2)

# newImage = tk.PhotoImage(file="day68/successday68.png")
# newImage = newImage.subsample(1, -2)

# container = canvas.create_image(150, 1, image=image)

# tk.mainloop()


from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("300x200")

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
    canvas.pack_forget()
    Warning.pack()
    return
  Warning.pack_forget()
  canvas.pack()


root = tk.Label(text="Guess Who?")
root.pack()

Warning = tk.Label(text="Unable to find this user")

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(text="Find!", command=showImage)
button.pack()

canvas = tk.Canvas(window, width=400, height=380)

Amy = ImageTk.PhotoImage(Image.open("day68/Amy.png"))
Bender = ImageTk.PhotoImage(Image.open("day68/Bender.png"))
Fry = ImageTk.PhotoImage(Image.open("day68/Fry.png"))
Leela = ImageTk.PhotoImage(Image.open("day68/Leela.png"))

container = canvas.create_image(150,1,image=Leela)

tk.mainloop()
