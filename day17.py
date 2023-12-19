# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit
# print("The game is over, you've failed!")


# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#     continue
# else:
#     print("Game over!")
#     exit()
# print("Thanks for playing!")


OPTIONS = ["rock", "paper", "scissors"]

playing = True

scoreplayer_1 = 0
scoreplayer_2 = 0

while playing:
    player1 = input("Player 1: What is your choice? (Rock, Paper, Scissors): ")
    player2 = input("Player 2: What is your choice? (Rock, Paper, Scissors): ")

    if player1 == player2:
        win = "Draw"
    elif player1 == "rock" and player2 == "scissors":
        scoreplayer_1 += 1
    elif player1 == "paper" and player2 == "rock":
        scoreplayer_1 += 1
    elif player1 == "scissors" and player2 == "paper":
        scoreplayer_1 += 1
    else:
        scoreplayer_2 += 1

    print("Player 1 has:", scoreplayer_1, "wins")
    print("Player 2 has:", scoreplayer_2, "wins")

    if scoreplayer_1 == 3 or scoreplayer_2 == 3:
        print("Thanks for playing!")
        playing = False
        exit()
    else:
        continue
