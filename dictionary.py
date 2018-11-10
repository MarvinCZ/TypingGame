import random
from word import Word


class Dictionary:
    def __init__(self):
        self.words = list(map(lambda x: Word(x), open('words.list', 'r').read().split("\n")))
        random.shuffle(self.words)
        self.index = 0

    def get(self):
        word = self.words[self.index]
        self.index += 1
        if self.index >= len(self.words):
            random.shuffle(self.words)
            self.index = 0
        return word
