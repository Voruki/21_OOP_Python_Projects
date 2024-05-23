class AdventureGame:
    def __init__(self):
        self.name = None  # Player's name

    def welcome(self):
        # Welcome the player and get their name
        self.name = input("Please type your name! ")
        print(f"Welcome {self.name} to this adventure!")

    def get_input(self, prompt, options):
        # Get user input and ensure it is one of the valid options
        while True:
            user_input = input(prompt).lower()
            if user_input in options:
                return user_input
            print("Not a valid option. You lose!")

    def dirt_road(self):
        # First decision point: left or right
        answer = self.get_input("You are on a dirt road, it has come to an end and now you can go left or right. Which way do you want to go? ", ["left", "right"])
        if answer == "left":
            self.left_path()
        elif answer == "right":
            self.right_path()

    def left_path(self):
        # Decision point for the left path: swim or walk
        answer = self.get_input("You come to a river, you can walk around it or swim across. (swim / walk) ", ["swim", "walk"])
        if answer == "swim":
            print("You swam across and were eaten by an alligator!")
        elif answer == "walk":
            print("You walked for many kilometers, ran out of water and you lost the game!")

    def right_path(self):
        # Decision point for the right path: cross or back
        answer = self.get_input("You come to a bridge and it looks wobbly. Do you want to cross it or head back? (cross / back) ", ["cross", "back"])
        if answer == "back":
            print("You go back and lose!")
        elif answer == "cross":
            self.cross_bridge()

    def cross_bridge(self):
        # Decision point after crossing the bridge: talk to the stranger or not
        answer = self.get_input("You cross the bridge and meet a stranger. Do you want to talk to them? (yes / no) ", ["yes", "no"])
        if answer == "yes":
            print("You talked to the stranger and they give you gold! You WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended! You lose!")

    def thank_you(self):
        # Thank the player for playing
        print(f"Thanks for playing, {self.name}!")

    def play(self):
        # Orchestrate the sequence of methods to play the game
        self.welcome()
        self.dirt_road()
        self.thank_you()

# Usage
if __name__ == "__main__":
    game = AdventureGame()  # Create an instance of AdventureGame
    game.play()  # Start the game

