import random

class NumberGuesser:
    def __init__(self):
        self.max_range = None  # Maximum range for random number generation
        self.random_number = None  # Random number to be guessed
        self.guesses = 0  # Counter for the number of guesses

    def get_max_range(self):
        # Prompt the user to input a valid maximum range
        while True:
            max_range = input("Please type an integer number: ")

            if max_range.isdigit():
                max_range = int(max_range)
                if max_range > 0:
                    self.max_range = max_range
                    break
                else:
                    print("Please type an integer number larger than 0!")
            else:
                print("Please type a valid integer number!")

    def generate_random_number(self):
        # Generate a random number within the specified range
        self.random_number = random.randint(0, self.max_range)

    def play_game(self):
        # Main game loop for guessing the number
        while True:
            self.guesses += 1
            user_guess = input("Please make a guess! ")

            # Ensure the user inputs a valid guess
            while not user_guess.isdigit():
                user_guess = input("Please make a valid guess! ")
            user_guess = int(user_guess)

            # Check if the user's guess is correct
            if user_guess == self.random_number:
                print("You guessed it RIGHT!")
                break
            elif user_guess < self.random_number:
                print("You were below the number!")
            else:
                print("You were above the number!")

    def display_result(self):
        # Display the result of the game
        print(f"You got the number in {self.guesses} guesses! Congratulations!")

    def play(self):
        # Orchestrate the sequence of methods to play the game
        self.get_max_range()
        self.generate_random_number()
        self.play_game()
        self.display_result()

# Usage
if __name__ == "__main__":
    guesser = NumberGuesser()  # Create an instance of NumberGuesser
    guesser.play()  # Start the game
