import random
import time

class MathQuiz:
    def __init__(self):
        self.operators = ["+", "-", "*"]
        self.min_operand = 3
        self.max_operand = 12
        self.total_problems = 10
        self.wrong_count = 0
        self.start_time = 0

    def generate_problem(self):
        """
        Generates a math problem consisting of two random operands and an operator.

        Returns:
        - tuple: A tuple containing the math expression as a string and the correct answer.
        """
        left = random.randint(self.min_operand, self.max_operand)
        right = random.randint(self.min_operand, self.max_operand)
        operator = random.choice(self.operators)

        expression = f"{left} {operator} {right}"
        answer = eval(expression)
        return expression, answer

    def start_quiz(self):
        """
        Starts the math quiz game.
        """
        start = input("Press Y to start! ").strip().capitalize()

        if start != "Y":
            print("Okay, bye!")
            return

        print("-------------------------------------")
        self.start_time = time.time()

        for i in range(self.total_problems):
            expression, answer = self.generate_problem()
            while True:
                guess = input(f"Problem #{i+1}: {expression} = ").strip()
                if guess == str(answer):
                    break
                else:
                    print("Incorrect, try again.")
                    self.wrong_count += 1

        self.end_quiz()

    def end_quiz(self):
        """
        Ends the math quiz game and displays the results.
        """
        end_time = time.time()
        total_time = round(end_time - self.start_time)

        print("-------------------------------------")
        if self.wrong_count == 0:
            print(f"Great work! You finished all in {total_time} seconds without any mistakes!")
        else:
            print(f"Nice work! You finished all in {total_time} seconds with {self.wrong_count} wrong answers.")

if __name__ == "__main__":
    quiz = MathQuiz()
    quiz.start_quiz()
