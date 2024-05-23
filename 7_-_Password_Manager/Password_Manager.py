from cryptography.fernet import Fernet
import os

class PasswordManager:
    def __init__(self):
        self.key_file = "key.key"
        self.password_file = "passwords.txt"
        self.fernet = self.load_or_generate_key()

    def load_or_generate_key(self):
        """
        Load the encryption key from file if it exists,
        otherwise generate a new key and save it to file.
        """
        if os.path.exists(self.key_file):
            return Fernet(self.load_key())
        else:
            key = Fernet.generate_key()
            self.write_key(key)
            return Fernet(key)

    def write_key(self, key):
        """
        Write the encryption key to file.
        """
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        """
        Load the encryption key from file.
        """
        with open(self.key_file, "rb") as key_file:
            return key_file.read()

    def encrypt_password(self, password):
        """
        Encrypt the password using the loaded Fernet instance.
        """
        return self.fernet.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        """
        Decrypt the password using the loaded Fernet instance.
        """
        return self.fernet.decrypt(encrypted_password.encode()).decode()

    def add_password(self):
        """
        Add a new password to the password file.
        """
        name = input("Account Name: ")
        password = input("Password: ")

        with open(self.password_file, "a") as file:
            encrypted_password = self.encrypt_password(password)
            file.write(f"{name} | {encrypted_password}\n")

    def view_passwords(self):
        """
        View existing passwords from the password file.
        """
        with open(self.password_file, "r") as file:
            for line in file.readlines():
                data = line.rstrip()
                name, encrypted_password = data.split(" | ")
                decrypted_password = self.decrypt_password(encrypted_password)
                print(f"User - {name} , Password - {decrypted_password}")

    def run(self):
        """
        Main loop for user interaction.
        """
        while True:
            mode = input("Would you like to add a new password, view existing ones, or quit? (add / view / q): ").lower()

            if mode == "q":
                break
            elif mode == "add":
                self.add_password()
            elif mode == "view":
                self.view_passwords()
            else:
                print("Invalid input. Please enter 'add', 'view', or 'q'.")

def main():
    manager = PasswordManager()
    manager.run()

if __name__ == "__main__":
    main()
