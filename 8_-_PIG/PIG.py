import random

class DiceGame:
    def __init__(self, max_score=50):
        self.max_score = max_score
        self.players = self.get_number_of_players()
        self.player_scores = [0] * self.players

    def get_number_of_players(self):
        """
        Get the number of players for the game (between 2 and 4).
        """
        while True:
            players = input("Enter the number of players (2-4): ")
            if players.isdigit():
                players = int(players)
                if 2 <= players <= 4:
                    return players
                else:
                    print("2 to 4 players only!")
            else:
                print("Invalid input. Please enter a number between 2 and 4.")

    def roll_dice(self):
        """
        Simulates rolling a six-sided die and returns the result.

        Returns:
        - int: Random number between 1 and 6.
        """
        min_value = 1
        max_value = 6
        return random.randint(min_value, max_value)

    def play_game(self):
        """
        Main game loop where players take turns rolling the dice.
        """
        while max(self.player_scores) < self.max_score:
            for player_index in range(self.players):
                print(f"\nPlayer {player_index + 1} is up!\n")
                print(f"Current total score: {self.player_scores[player_index]}\n")
                current_score = 0

                while True:
                    option_roll = input("Roll the dice? [y/n]: ")
                    if option_roll.lower() != "y":
                        break

                    value = self.roll_dice()
                    if value == 1:
                        print("You rolled a 1! Turn ends with no points.")
                        current_score = 0
                        break
                    else:
                        current_score += value
                        print(f"You rolled a {value}!")

                    print(f"Current round score: {current_score}")

                self.player_scores[player_index] += current_score
                print(f"Player {player_index + 1} total score: {self.player_scores[player_index]}")

        max_score = max(self.player_scores)
        winning_index = self.player_scores.index(max_score)
        print(f"\nPlayer {winning_index + 1} wins with a score of {max_score}!")

def main():
    game = DiceGame()
    game.play_game()

if __name__ == "__main__":
    main()
