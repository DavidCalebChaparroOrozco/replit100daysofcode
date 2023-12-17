# Define the three options for the game
OPTIONS = ["rock", "paper", "scissors"]

# Start the game
playing = True

while playing:

    # Get the player 1's move
    player1 = input("Player 1: What is your move? (rock, paper, or scissors): ")

    # Get the player 2's move
    player2 = input("Player 2: What is your move? (rock, paper, or scissors): ")

    # Determine the winner of the game
    if player1 == player2:
        winner = "Tie"
    elif player1 == "rock" and player2 == "scissors":
        winner = "Player 1"
    elif player1 == "paper" and player2 == "rock":
        winner = "Player 1"
    elif player1 == "scissors" and player2 == "paper":
        winner = "Player 1"
    else:
        winner = "Player 2"

    # Print the results of the game
    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")
    print(f"Winner: {winner}")

    # Ask if we want to keep playing
    playing = input("Do you want to keep playing? (y/n): ")
    playing = playing.lower() == "y"
