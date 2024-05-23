class Quiz:
    def __init__(self):
        self.score = 0  # Initialize the score to zero

    def welcome(self):
        print("Welcome to a short quiz game!")  # Welcome message

    def play(self):
        # Ask the user if they want to play and return True if the answer is 'yes'
        play_option = input("Do you want to play? [yes,no] ").lower()
        return play_option == "yes"

    def ask_question(self, question, answer):
        # Ask a question and check if the answer is correct
        user_answer = input(question).lower()
        if user_answer == answer:
            print("Correct!")
            self.score += 1  # Increment score for a correct answer
        else:
            print("Incorrect!")

    def run_quiz(self):
        # Run the quiz by welcoming the user and asking questions
        self.welcome()
        if not self.play():
            quit()  # Exit the quiz if the user does not want to play

        # List of questions and answers
        questions_and_answers = [
            ("What does CPU stand for? ", "central processing unit"),
            ("What does GPU stand for? ", "graphics processing unit"),
            ("What does RAM stand for? ", "random access memory"),
            ("What does PSU stand for? ", "power supply")
        ]

        # Ask each question from the list
        for question, answer in questions_and_answers:
            self.ask_question(question, answer)

        # Print the final score and percentage
        print(f"Congratulations! You scored {self.score} out of {len(questions_and_answers)} questions!")
        print(f"You scored {(self.score / len(questions_and_answers)) * 100:.2f}%!")

if __name__ == "__main__":
    quiz = Quiz()  # Create a Quiz object
    quiz.run_quiz()  # Start the quiz
