import curses
from curses import wrapper
import time
import random

class WpmTypingTest:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.target_text = self.load_text()
        self.current_text = []
        self.wpm = 0

    def start_screen(self):
        """
        Displays the start screen and waits for user input to begin the test.
        """
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Welcome to the WPM Typing Test!")
        self.stdscr.addstr("\nPress any key to begin!")
        self.stdscr.refresh()
        self.stdscr.getkey()

    def load_text(self):
        """
        Loads a random line from the text file for the typing test.
        """
        with open("text.txt", "r") as file:
            lines = file.readlines()
            return random.choice(lines).strip()

    def display_text(self):
        """
        Displays the target text, current input text, and WPM on the screen.
        """
        self.stdscr.addstr(0, 0, self.target_text)
        self.stdscr.addstr(1, 0, f"WPM: {self.wpm}")

        for i, char in enumerate(self.current_text):
            correct_char = self.target_text[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            self.stdscr.addstr(0, i, char, color)

    def wpm_test(self):
        """
        Executes the WPM typing test.
        """
        start_time = time.time()
        self.stdscr.nodelay(True)

        while True:
            time_elapsed = max(time.time() - start_time, 1)
            self.wpm = round((len(self.current_text) / (time_elapsed / 60)) / 5)

            self.stdscr.clear()
            self.display_text()
            self.stdscr.refresh()

            if "".join(self.current_text) == self.target_text:
                self.stdscr.nodelay(False)
                break

            try:
                key = self.stdscr.getkey()
            except:
                continue

            if ord(key) == 27:
                break
            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if len(self.current_text) > 0:
                    self.current_text.pop()
            elif len(self.current_text) < len(self.target_text):
                self.current_text.append(key)

    def main(self):
        """
        Main function to run the typing test.
        """
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        self.start_screen()
        while True:
            self.wpm_test()
            self.stdscr.addstr(2, 0, "You completed the text! Press any key to continue!")
            key = self.stdscr.getkey()
            if ord(key) == 27:
                break

def main(stdscr):
    test = WpmTypingTest(stdscr)
    test.main()

if __name__ == "__main__":
    wrapper(main)

