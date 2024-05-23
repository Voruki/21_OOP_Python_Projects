import random

# Define constants for colors, number of tries, and code length
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    """
    Generates a random code consisting of colors from the COLORS list.

    Returns:
    - list: A list of randomly chosen colors.
    """
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def guess_code():
    """
    Prompts the user to guess the code and validates the input.

    Returns:
    - list: A list of guessed colors.
    """
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors!")
            continue

        if all(color in COLORS for color in guess):
            return guess
        else:
            print(f"Invalid color(s) detected. Valid colors are: {', '.join(COLORS)}. Try again!")

def check_code(guess, real_code):
    """
    Checks the guessed code against the real code and counts correct and incorrect positions.

    Args:
    - guess (list): The guessed code.
    - real_code (list): The real code.

    Returns:
    - tuple: Number of correct positions and incorrect positions.
    """
    color_counts = {color: real_code.count(color) for color in COLORS}
    correct_pos = sum(1 for guess_color, real_color in zip(guess, real_code) if guess_color == real_color)

    incorrect_pos = 0
    for guess_color in guess:
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    incorrect_pos -= correct_pos
    return correct_pos, incorrect_pos

def game():
    """
    Runs the Mastermind game.
    """
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code...")
    print("The valid colors are:", ', '.join(COLORS))

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries. The code was:", ' '.join(code))

if __name__ == "__main__":
    game()
