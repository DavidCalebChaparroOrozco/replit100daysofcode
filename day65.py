class character:
  name = None
  hp = 100
  mp = 100

  def __init__(self, name):
    self.name = name

  def prettyPrint(self):
    print(f"{self.name}\t HP: {self.hp}\t SP: {self.mp}")

  def setStats(self, hp, mp):
    self.hp = hp
    self.mp = mp

class player(character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def prettyPrint(self):
    print(f"{self.name}\t HP: {self.hp}\t SP: {self.mp}\t Nickname: {self.nickname}\t Lives: {self.lives}")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has died!")
      return False

Vlad = player("Vladictor")
Vlad.prettyPrint()
print(Vlad.isAlive())

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def prettyPrint(self):
    print(f"{self.name}\t HP: {self.hp}\t SP: {self.mp}\t Type: {self.type}\t Strength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def prettyPrint(self):
    print(f"{self.name}\t HP: {self.hp}\t SP: {self.mp}\t Type: {self.type}\t Strength: {self.strength}\t Speed: {self.speed}")

Shrek = orc(250)
Shrek.prettyPrint()

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def prettyPrint(self):
    print(f"{self.name}\t HP: {self.hp}\t SP: {self.mp}\t Type: {self.type}\t Strength: {self.strength}\t Day: {self.day}")

Dracula = vampire(False)
Dracula.prettyPrint()
