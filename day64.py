# class animal:
#   species = None
#   name = None
#   sound = None
#   # Sets the characteristics
 
#   def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
#     self.name = name
#     self.species = species
#     self.sound = sound
#     self.color = color
#     # 'self' means 'this object'

#   def talk(self):
#     print((f"{self.name} says {self.sound}"))


  
# dog = animal("Brian", "Canine", "Woof", "brown")
# print(dog.sound)
# dog.talk()

# cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
# print(cow.sound)
# cow.talk()



# class animal:
#   species = None
#   name = None
#   sound = None

#   def __init__(self, name, species, sound):
#     self.name = name
#     self.species = species
#     self.sound = sound

#   def talk(self):
#     print((f"{self.name} says {self.sound}"))
  
# class bird(animal):

#   def __init__(self, color):
#     self.name = "Bird"
#     self.species = "Avian"
#     self.sound = "Tweet"
#     self.color = color # Only applies to the bird sub class


# polly = bird("Green") # Sets polly's colour to 'Green'
# polly.talk()
# print(polly.color) # Prints polly's color



class jobs:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked


  def prettyPrint(self):
    print(" Job ".center(50, "="))
    print()
    print(f"{self.name:<10}: {self.salary:^10} {self.hoursWorked:>10}")

class doctor(jobs):
  exp = None
  speciality = None

  def __init__(self, salary, hoursWorked, exp, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.exp = exp
    self.speciality = speciality

  def prettyPrint(self):
    print(" Job ".center(50, "="))
    print()
    print(f"{self.name:<10}: {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.exp:<10} {self.speciality:>21}")

class teacher(jobs):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position

  def prettyPrint(self):
    print(" Job ".center(50, "="))
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")


lawyer = jobs("Lawyer", "$150,000", "25")
lawyer.prettyPrint()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.prettyPrint()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.prettyPrint()
