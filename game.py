import pygame
from dictionary import Dictionary
import renderer


class Game:
    WORDS_MARGIN_TOP = 20
    WIDTH = 620
    HEIGHT = 320
    WORD_FONT_SIZE = 25
    WORD_MARGIN = 5
    DEFAULT_FONT = 'MonoSpace'
    DEFAULT_WORD_COLOR = (0,0,0)

    def __init__(self):
        self.player = None
        self.enemy = None
        self.dictionary = Dictionary()
        self.font = pygame.font.SysFont(Game.DEFAULT_FONT, Game.WORD_FONT_SIZE)

        self.words = [self.dictionary.get() for i in range(5)]
        self.letters = []

    def draw_words(self, screen):
        valid_words, _ = self.get_valid_words(self.letters)
        for i in range(len(self.words)):
            top = i * Game.WORD_FONT_SIZE + Game.WORDS_MARGIN_TOP
            label, rectangle = renderer.text_objects(self.font, self.words[i], Game.DEFAULT_WORD_COLOR, (Game.WIDTH/2, top + Game.WORD_FONT_SIZE/2))
            if i in valid_words and len(self.letters) > 0:
                count_of_letters = len(self.words[i])
                new_rectangle = pygame.Rect(rectangle.left, rectangle.top, rectangle.width * (len(self.letters) / count_of_letters), rectangle.height)
                pygame.draw.rect(screen, (255,255,255), new_rectangle)

            screen.blit(label, rectangle)

    def draw(self, screen):
        screen.fill((110, 191, 191))
        self.draw_words(screen)

    def handle_key(self, key):
        letter = self.get_letter(key)
        if letter:
            new_letters = list(self.letters)
            new_letters.append(letter)
            valid_words, complete_words = self.get_valid_words(new_letters)
            if valid_words:
                if complete_words:
                    self.letters = []
                    self.word_completed(complete_words[0])
                else:
                    self.letters = new_letters

    def get_valid_words(self, letters):
        valid_words = []
        completed_words = []
        for i in range(len(self.words)):
            ok = True
            for j in range(len(letters)):
                if len(self.words[i]) <= j or letters[j] != self.words[i][j].lower():
                    ok = False
                    break
            if ok:
                valid_words.append(i)
                if len(self.words[i]) == len(letters):
                    completed_words.append(self.words[i])
        return valid_words, completed_words

    @staticmethod
    def get_letter(key):
        if 97 <= key <= 122:
            return chr(key)
        return None

    def word_completed(self, word):
        self.words.remove(word)
        self.words.append(self.dictionary.get())
        pass

