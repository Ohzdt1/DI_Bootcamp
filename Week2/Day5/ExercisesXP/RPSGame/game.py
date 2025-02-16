import random

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Prompt user for input and validate choice."""
        while True:
            user_choice = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_choice in ["r", "p", "s"]:
                return {"r": "rock", "p": "paper", "s": "scissors"}[user_choice]
            print("Invalid choice, please try again.")

    def get_computer_item(self):
        """Randomly select rock, paper, or scissors for the computer."""
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        """Determine the winner."""
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        """Run a single round of Rock-Paper-Scissors."""
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)

        print(f"You chose: {user_choice}. The computer chose: {computer_choice}. Result: {result}")

        return result