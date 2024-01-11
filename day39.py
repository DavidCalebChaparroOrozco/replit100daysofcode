import random, os, time

listOfWords = [
  "british", "suave", "integrity", "accent", "evil", "genius", "Downton",
  "apple", "orange", "banana", "grape", "pear", "peach", "mango", "straw"
]
letterPicked = []
lives = 5
wordChosen = random.choice(listOfWords)

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()

  if letter in letterPicked:
    print("You've tried that before")
    continue
  letterPicked.append(letter)

  if letter in wordChosen:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1

  allLetters = True
  for i in wordChosen:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False

  if allLetters:
    print(f"You won with {lives} left!")

  if lives <= 0:
    print(f"You ran out of lives! The answer was {wordChosen}")
    break
  else:
    print(f"Only {lives} left")
