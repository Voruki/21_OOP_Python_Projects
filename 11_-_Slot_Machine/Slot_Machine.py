import random


class SlotMachine:
    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1

    ROWS = 3
    COLS = 3

    symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
    symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

    def __init__(self):
        self.balance = 0

    def deposit(self):
        """
        Prompts the user to deposit money into their balance.
        """
        while True:
            amount = input("How much would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    self.balance += amount
                    break
                else:
                    print("Amount must be greater than 0!")
            else:
                print("Please enter numbers only!")

    def get_number_of_lines(self):
        """
        Prompts the user to enter the number of lines to bet on.
        """
        while True:
            lines = input(f"Enter the number of lines to bet on. (1 - {self.MAX_LINES}) ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= self.MAX_LINES:
                    break
                else:
                    print(f"Lines must be between 1 and {self.MAX_LINES}!")
            else:
                print("Please enter number only!")

        return lines

    def get_bet(self):
        """
        Prompts the user to enter the bet amount for each line.
        """
        while True:
            bet = input("How much would you like to bet on each line? $")
            if bet.isdigit():
                bet = int(bet)
                if self.MIN_BET <= bet <= self.MAX_BET:
                    break
                else:
                    print(f"Amount must be between ${self.MIN_BET} and ${self.MAX_BET}!")
            else:
                print("Please enter numbers only!")

        return bet

    def get_slot_machine_spin(self):
        """
        Generates a spin result for the slot machine.
        """
        all_symbols = []
        for symbol, count in self.symbol_count.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(self.COLS):
            column = random.sample(all_symbols, self.ROWS)
            columns.append(column)

        return columns

    def print_slot_machine(self, columns):
        """
        Prints the slot machine grid.
        """
        for row in range(self.ROWS):
            for i, column in enumerate(columns):
                if i != len(column) - 1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")
            print()

    def check_winnings(self, columns, lines, bet):
        """
        Checks for winnings based on the spin result.
        """
        winnings = 0
        winning_lines = []

        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                if symbol != column[line]:
                    break
            else:
                winnings += self.symbol_value[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines

    def spin(self):
        """
        Executes a spin round of the slot machine.
        """
        lines = self.get_number_of_lines()

        while True:
            bet = self.get_bet()
            total_bet = bet * lines

            if total_bet > self.balance:
                print("You do not have enough money to bet that amount!")
                print(f"You current balance is only ${self.balance}!")
            else:
                break

        print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

        slots = self.get_slot_machine_spin()
        self.print_slot_machine(slots)

        winnings, winning_lines = self.check_winnings(slots, lines, bet)
        print(f"You won ${winnings}!")
        if winning_lines:
            print(f"You won on lines: ", *winning_lines)

        self.balance += winnings - total_bet
        return winnings - total_bet

    def play(self):
        """
        Main function to run the slot machine game.
        """
        self.deposit()

        while True:
            print(f"Current balance is: ${self.balance}")
            answer = input("Press enter to play. (q to quit) ").strip()
            if answer.lower() == "q":
                break
            self.balance += self.spin()

        print(f"You left with ${self.balance}!")


if __name__ == "__main__":
    slot_machine = SlotMachine()
    slot_machine.play()
