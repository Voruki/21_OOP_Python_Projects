class StoryProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.story = self.read_story()
        self.placeholders = self.extract_placeholders()
        self.answers = {}

    def read_story(self):
        """
        Read the content of the story file.
        """
        with open(self.file_path, "r") as file:
            return file.read()

    def extract_placeholders(self):
        """
        Extract placeholders from the story and return them as a set.
        """
        placeholders = set()
        start_of_word = -1
        target_start = "<"
        target_end = ">"

        for i, char in enumerate(self.story):
            if char == target_start:
                start_of_word = i
            if char == target_end and start_of_word != -1:
                word = self.story[start_of_word:i + 1]
                placeholders.add(word)
                start_of_word = -1

        return placeholders

    def prompt_user_for_answers(self):
        """
        Prompt the user to input words for each placeholder and store them in self.answers.
        """
        for word in self.placeholders:
            answer = input(f"Enter a word for {word}: ")
            self.answers[word] = answer

    def replace_placeholders(self):
        """
        Replace placeholders in the story with user-provided words.
        """
        for word in self.placeholders:
            self.story = self.story.replace(word, self.answers[word])

    def print_story(self):
        """
        Print the modified story with replaced placeholders.
        """
        print(self.story)

    def process_story(self):
        """
        Perform the entire process of reading, extracting placeholders,
        prompting for answers, replacing placeholders, and printing the story.
        """
        self.prompt_user_for_answers()
        self.replace_placeholders()
        self.print_story()


# Example usage:
if __name__ == "__main__":
    file_path = "story.txt"
    processor = StoryProcessor(file_path)
    processor.process_story()
