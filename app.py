import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ["yes", "no"]:
            return choice == "yes"
        else:
            print("Invalid choice. Please try again.")

def display_score(player_score, computer_score):
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "player":
            print("You won!")
            player_score += 1
        elif winner == "computer":
            print("You lost!")
            computer_score += 1
        else:
            print("It's a tie!")

        display_score(player_score, computer_score)

        if not play_again():
            break

play_game()
