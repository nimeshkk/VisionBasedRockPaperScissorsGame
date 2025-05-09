import random

def get_computer_choice():
    """Return a random gesture choice for the computer."""
    return random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])

def determine_winner(user, computer):
    """Determine the winner of the game."""
    if user == computer:
        return "It's a tie!"
    winning_combinations = {
        "Rock": ["Scissors", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Spock", "Paper"],
        "Spock": ["Scissors", "Rock"]
    }
    if computer in winning_combinations[user]:
        return "You win!"
    return "Computer wins!"