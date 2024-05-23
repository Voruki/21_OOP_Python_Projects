import random
import string

class PasswordGenerator:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special = string.punctuation

    def generate_password(self, min_length, numbers=True, special_characters=True):
        """
        Generate a random password with specified criteria.

        Args:
        - min_length (int): Minimum length of the password.
        - numbers (bool): Whether to include numbers in the password.
        - special_characters (bool): Whether to include special characters in the password.

        Returns:
        - str: Generated password meeting the specified criteria.
        """
        characters = self.letters
        if numbers:
            characters += self.digits
        if special_characters:
            characters += self.special

        password = ""
        meet_criteria = False
        has_number = False
        has_special = False

        while len(password) < min_length or not meet_criteria:
            new_char = random.choice(characters)
            password += new_char

            if new_char in self.digits:
                has_number = True
            elif new_char in self.special:
                has_special = True

            meet_criteria = True
            if numbers:
                meet_criteria = has_number
            if special_characters:
                meet_criteria = meet_criteria and has_special

        return password

def main():
    generator = PasswordGenerator()

    # Get user input
    min_length = int(input("Enter the minimum length: "))
    has_number = input("Do you want to include numbers? [Y/N] ").lower() == "y"
    has_special = input("Do you want to include special characters? [Y/N] ").lower() == "y"

    # Generate password
    pwd = generator.generate_password(min_length, has_number, has_special)
    print(f"The generated password is: {pwd}")

if __name__ == "__main__":
    main()
