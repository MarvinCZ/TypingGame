import pygame
from dictionary import Dictionary
from player import Player
from enemy import Enemy
from renderer import Renderer


class Game:

    WORDS_COUNT = 3

    def __init__(self):
        self.player = Player()
        self.enemy = Enemy(name='Cthulhu')
        self.dictionary = Dictionary()
        self.win = False
        self.loss = False

        self.words = [self.dictionary.get() for i in range(Game.WORDS_COUNT)]
        self.letters = []

        self.renderer = Renderer()

    def draw(self):
        self.renderer.draw_background()
        self.renderer.render_words(self.words, self.get_valid_words(self.letters), len(self.letters))
        self.renderer.render_player_health_bar(self.player.max_health, self.player.health)
        self.renderer.render_enemy_health_bar(self.enemy.max_health, self.enemy.health)
        self.renderer.render_experience_bar(100, 55)
        self.renderer.render_time_bar(self.enemy.damage_time, int(self.enemy.timer() * 1000))

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
            self.handle_new_latter(letter)

    def handle_new_latter(self, letter):
        new_letters = self.letters + [letter]
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
        self.fill_words()

    def fill_words(self):
        while len(self.words) < Game.WORDS_COUNT:
            self.words.append(self.dictionary.get())
