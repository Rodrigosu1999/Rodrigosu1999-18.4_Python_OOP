"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """
    The class will create a list for each line of  text from a file
    """

    def __init__(self, txt_file, words_list=[]):
        """
        The initializer will give us an empty list and  run the return_text_list function to fill the list
        """
        self.words_list = words_list
        self.txt_file = self.return_text_list(txt_file, words_list)

    def random(self):
        random_index = random.randint(0, len(self.words_list) - 1)
        return self.words_list[random_index]

    def return_text_list(self, txt_file, list):
        """
        The function will append to the empty list all lines of text
        """
        file = open(txt_file, "r")
        count = 0
        for line in file:
            count = count + 1
            list.append(line.rstrip("\n"))
        file.close()
        print(f"There were {count} words read")


class SpecialWordFinder(WordFinder):
    """
    Here we are retrieving the basic functionality (methods) from the WordFinder Class
    """

    def __init__(self, txt_file):
        """
    Here we are retrieving the basic functionality  from the WordFinder Class
    """
        super().__init__(txt_file)

    def return_text_list(self, txt_file, list):
        """
    The function will append to the empty list all lines of text if the line is not empty or it starts with a "#"
    """
        file = open(txt_file, "r")
        count = 0
        for line in file:
            if not line.startswith("#") and not line.startswith("\n"):
                count = count + 1
                list.append(line.rstrip("\n"))
        file.close()
        print(f"There were {count} words read")
