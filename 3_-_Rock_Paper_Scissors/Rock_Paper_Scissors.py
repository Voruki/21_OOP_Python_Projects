import random

class RockPaperScissors:
    def __init__(self):
        self.user_wins = 0  # Counter for user wins
        self.computer_wins = 0  # Counter for computer wins
        self.options = ["rock", "paper", "scissors"]  # Available options for the game

    def play_round(self):
        # Main game loop to play rounds of Rock, Paper, Scissors
        while True:
            user_input = input("Type Rock / Paper / Scissors or Q to quit: ").lower()
            if user_input == "q":
                break  # Exit the game loop if user wants to quit

            if user_input not in self.options:
                continue  # Continue if the user input is invalid

            # Computer randomly picks an option
            random_number = random.randint(0, 2)
            comp_pick = self.options[random_number]
            print(f"The computer has picked {comp_pick}!")
            print("----------------------------------------------------")

            # Determine the winner
            if (user_input == "rock" and comp_pick == "scissors") or \
               (user_input == "paper" and comp_pick == "rock") or \
               (user_input == "scissors" and comp_pick == "paper"):
                print("You won!")
                print("----------------------------------------------------")
                self.user_wins += 1  # Increment user win counter
            elif user_input == comp_pick:
                print("Draw!")
                print("----------------------------------------------------")
            else:
                print("You lost!")
                print("----------------------------------------------------")
                self.computer_wins += 1  # Increment computer win counter

    def display_results(self):
        # Display the final results after quitting the game
        print("----------------------------------------------------")
        print(f"You have won {self.user_wins} times!")
        print(f"The computer has won {self.computer_wins} times!")
        print("Goodbye!")

    def play(self):
        # Orchestrate the sequence of methods to play the game
        self.play_round()
        self.display_results()

# Usage
if __name__ == "__main__":
    game = RockPaperScissors()  # Create an instance of RockPaperScissors
    game.play()  # Start the game
