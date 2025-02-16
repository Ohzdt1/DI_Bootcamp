import os

class AnagramChecker:
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), "words.txt")

        if not os.path.exists(file_path):
            raise FileNotFoundError("Error: words.txt file not found.")

        with open(file_path, "r", encoding="utf-8") as file:
            self.words = set(word.strip().lower() for word in file.readlines())

    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        word = word.lower()
        return [w for w in self.words if self.is_anagram(word, w) and w != word]
