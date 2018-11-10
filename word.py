class Word:
    def __init__(self, word):
        self.word = word

    def is_valid(self, letters):
        ok = True
        for i in range(len(letters)):
            if len(self.word) <= i or letters[i] != self.word[i].lower():
                ok = False
                break
        return ok

    def is_complete(self, letters):
        return self.is_valid(letters) and len(letters) == len(self.word)

    def damage(self, base_damage):
        return int((len(self.word) * base_damage)/100)
