import tkinter as tk

window = tk.Tk()
window.title("Visual Novel with Rick Sanchez")
window.geometry("400x400")

story = "You come across a strange portal, what do you do?"

def iCode():
  global story
  canvas.itemconfig(container, image=codes)
  story = "You meet Rick drinking a beer at his house"
  storyLabel["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button3.pack()
  button4.pack()

def iReplit():
  global story
  canvas.itemconfig(container, image=replit)
  story = "What are you doing in my house?"
  storyLabel["text"] = story
  button.pack_forget()
  button2.pack_forget()
  button5.pack()
  button6.pack()

def iEdit():
  global story
  canvas.itemconfig(container, image=vs)
  story = "You share with him a beer that you carry"
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()

def iUse():
  global story
  canvas.itemconfig(container, image=amazing)
  story = "Rick accepts your offering and invites you on an adventure."
  storyLabel["text"] = story
  button3.pack_forget()
  button4.pack_forget()
  restartButton.pack()

def iToo():
  global story
  canvas.itemconfig(container, image=days)
  story = "You go to the adventure"
  storyLabel["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  restartButton.pack()

def iWin():
  global story
  canvas.itemconfig(container, image=amazing)
  story = "You enjoy the adventure and say goodbye to Rick to meet in a future adventure."
  storyLabel["text"] = story
  button5.pack_forget()
  button6.pack_forget()
  restartButton.pack()

def restart():
  global story
  canvas.itemconfig(container, image=start)
  story = "You come across a strange portal, what do you do?"
  storyLabel["text"] = story
  restartButton.pack_forget()
  button.pack()
  button2.pack()

start = tk.PhotoImage(file="day69/day69rickandmorty1.png")
start = start.subsample(4)

codes = tk.PhotoImage(file="day69/day69rickandmorty2.png")
codes = codes.subsample(4)

replit = tk.PhotoImage(file="day69/day69rickandmorty3.png")
replit = replit.subsample(4)

days = tk.PhotoImage(file="day69/day69rickandmorty4.png")
days = days.subsample(4)

amazing = tk.PhotoImage(file = "day69/day69rickandmorty5.png")
amazing = amazing.subsample(4)

vs = tk.PhotoImage(file = "day69/day69rickandmorty6.png")
vs = vs.subsample(4)

canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()

container = canvas.create_image(150,150,image=start)

storyLabel = tk.Label(text=story)
storyLabel.pack()

button = tk.Button(text="You enter the portal", command=iCode)
button.pack()

button2 = tk.Button(text="You are pushed into the portal", command=iReplit)
button2.pack()

button3 = tk.Button(text="You greet him casually", command=iEdit)

button4 = tk.Button(text="You greet rudely", command=iUse)

button5 = tk.Button(text="You explain the situation", command=iToo)

button6 = tk.Button(text="You offer to help", command=iWin)

restartButton = tk.Button(text="Restart", command=restart)

tk.mainloop()
