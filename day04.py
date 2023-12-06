print("""
Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!
""")

nameHero = input("What is your name?: ")
nameEnemy = input("What is worst enemy's name?: ")
superpowerHero = input("What is your superpower?: ")
liveHero = input("Where do you live?: ")
foodHero = input("What is your favorite food?: ")
print("\033[34m", "Hello", nameHero, "Your ability to", superpowerHero,
      "will make sure you never have to look at", nameEnemy, "again.",
      "Go eat", foodHero, "as you walk down the streets of", liveHero,
      "and use", superpowerHero, "for good and not evil!")
