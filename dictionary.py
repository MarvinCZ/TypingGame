import random


class Dictionary:
    def __init__(self):
        self.words = ['ahoj', 'lorem', 'ipsum', 'ypsum', 'dolores', 'ahmed', 'alah', 'trautemberk', 'lora', 'lore']
        random.shuffle(self.words)
        self.index = 0

    def get(self):
        word = self.words[self.index]
        self.index += 1
        if self.index >= len(self.words):
            random.shuffle(self.words)
            self.index = 0
        return word
