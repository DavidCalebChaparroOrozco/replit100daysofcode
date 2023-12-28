from replit import audio
import os, time

# print("Welcome")
# print("to")
# print("Replit")

# time.sleep(1)
# os.system("clear")

# username = input("Username: ")

def play():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    user = int(input("Press 2 anytime to stop playback and go back to the menu: "))
    if user == 2:
      source.paused = True
      return
    else:
      continue

while True:
  os.system("clear")
  print("Press 1 to play song")
  time.sleep(1)
  print("Press 2 to exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Play some songs")
    play()
  elif userInput == 2:
    exit()
  else:
    continue
