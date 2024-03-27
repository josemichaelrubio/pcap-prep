"""
The program I wrote
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        valid_choices = ["rock", "paper", "scissors"]
        while True:
            choice = input("Enter your choice (rock/paper/scissors): ").lower()
            if choice in valid_choices:
                self.choice = choice
                break
            else:
                print("Invalid choice. Please try again.")

class Computer:
    def __init__(self):
        self.name = "Computer"
        self.choice = None

    def choose(self):
        valid_choices = ["rock", "paper", "scissors"]
        self.choice = random.choice(valid_choices)

def determine_winner(player, computer):
    if player.choice == computer.choice:
        return "It's a tie!"
    elif (player.choice == "rock" and computer.choice == "scissors") or \
         (player.choice == "paper" and computer.choice == "rock") or \
         (player.choice == "scissors" and computer.choice == "paper"):
        return f"{player.name} wins!"
    else:
        return f"{computer.name} wins!"


def play_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    computer = Computer()

    player.choose()
    computer.choose()

    print(f"{player.name} chose {player.choice}")
    print(f"{computer.name} chose {computer.choice}")

    print(determine_winner(player, computer))

play_game()

