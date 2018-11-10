import pygame
from dictionary import Dictionary
import renderer
from player import Player
from enemy import Enemy


class Game:

    WORDS_COUNT = 3
    WORDS_MARGIN_TOP = 20
    WIDTH = 480
    HEIGHT = 640
    WORD_FONT_SIZE = 32
    WORD_MARGIN = 5
    DEFAULT_FONT_BOLD = 'Inconsolata-Bold.ttf'
    DEFAULT_FONT_REGULAR = 'Inconsolata-Regular.ttf'
    WORD_COLOR = (52, 52, 52)
    BACKGROUND_COLOR = (56, 119, 119)
    WORD_HIGHLIGHT_COLOR = (153, 179, 179)

    def __init__(self):
        self.player = Player()
        self.enemy = Enemy(name='Cthulhu')
        self.dictionary = Dictionary()
        self.font = pygame.font.Font(Game.DEFAULT_FONT_BOLD, Game.WORD_FONT_SIZE)
        self.win = False
        self.loss = False

        self.words = [self.dictionary.get() for i in range(Game.WORDS_COUNT)]
        self.letters = []

    def draw_words(self, screen):
        valid_words = self.get_valid_words(self.letters)
        for i in range(len(self.words)):
            top = i * Game.WORD_FONT_SIZE + Game.WORDS_MARGIN_TOP
            label, rectangle = renderer.text_objects(self.font, self.words[i].word.upper(), Game.WORD_COLOR, (Game.WIDTH/2, top + Game.WORD_FONT_SIZE/2))
            if self.words[i] in valid_words and len(self.letters) > 0:
                count_of_letters = len(self.words[i].word)
                new_rectangle = pygame.Rect(rectangle.left, rectangle.top, rectangle.width * (len(self.letters) / count_of_letters), rectangle.height)
                pygame.draw.rect(screen, Game.WORD_HIGHLIGHT_COLOR, new_rectangle)

            screen.blit(label, rectangle)
        self.draw_attributes(screen)

    def draw_attributes(self, screen):
        attributes = "BossHealth: {}\nPlayerHeath: {}\nTimer: {}".format(self.enemy.health, self.player.health, self.enemy.timer())
        print(attributes)

    def draw(self, screen):
        screen.fill(Game.BACKGROUND_COLOR)
        self.draw_words(screen)

    def tick(self, events):

        if self.enemy.health <= 0:
            self.win = True
        if self.player.health <= 0:
            self.loss = True

        if not self.loss and not self.win:
            self.enemy.process_channeling(self.player)
            for event in events:
                if event.type == pygame.KEYUP:
                    self.handle_key(event.key)

    def handle_key(self, key):
        letter = self.get_letter(key)
        if letter:
            new_letters = list(self.letters)
            new_letters.append(letter)
            valid_words = self.get_valid_words(new_letters)
            if valid_words:
                complete_words = self.get_completed_words(new_letters)
                if complete_words:
                    self.letters = []
                    self.word_completed(complete_words)
                else:
                    self.letters = new_letters

    def get_valid_words(self, letters):
        return [x for x in self.words if x.is_valid(letters)]

    def get_completed_words(self, letters):
        return [x for x in self.words if x.is_complete(letters)]

    @staticmethod
    def get_letter(key):
        if 97 <= key <= 122:
            return chr(key)
        return None

    def word_completed(self, words):
        if type(words) != list:
            words = [words]

        for word in words:
            self.enemy.hit(word.damage(self.player.base_damage), self.player)
            self.words.remove(word)
            self.words.append(self.dictionary.get())


