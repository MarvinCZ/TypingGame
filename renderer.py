import pygame


class Renderer:
    WIDTH = 480
    HEIGHT = 640
    WORD_FONT_SIZE = 32
    WORDS_MARGIN_TOP = 50
    WORD_COLOR = (52, 52, 52)
    BACKGROUND_COLOR = (56, 119, 119)
    WORD_HIGHLIGHT_COLOR = (153, 179, 179)
    DEFAULT_FONT_BOLD = 'Inconsolata-Bold.ttf'
    DEFAULT_FONT_REGULAR = 'Inconsolata-Regular.ttf'

    def __init__(self):
        self.screen = pygame.display.set_mode((Renderer.WIDTH, Renderer.HEIGHT))
        self.font = pygame.font.Font(Renderer.DEFAULT_FONT_BOLD, Renderer.WORD_FONT_SIZE)

    def text_objects(self, text, color, text_center):
        rendered = self.font.render(text, True, color)
        return rendered, rendered.get_rect(center=text_center)

    def draw_background(self):
        self.screen.fill(Renderer.BACKGROUND_COLOR)

    def render_health_bar(self, max_health, current_health):
        health_bar = pygame.Rect()
        pygame.draw.rect(self.screen, (255, 0, 0), health_bar)

    def render_words(self, words, valid_words, current_letter_count):
        for i in range(len(words)):
            top = i * Renderer.WORD_FONT_SIZE + Renderer.WORDS_MARGIN_TOP
            label, rectangle = self.text_objects(words[i].word.upper(), Renderer.WORD_COLOR, (Renderer.WIDTH / 2, top + Renderer.WORD_FONT_SIZE / 2))

            if words[i] in valid_words and current_letter_count > 0:
                count_of_letters = len(words[i].word)
                new_rectangle = pygame.Rect(rectangle.left, rectangle.top, rectangle.width * (current_letter_count / count_of_letters), rectangle.height)
                pygame.draw.rect(self.screen, Renderer.WORD_HIGHLIGHT_COLOR, new_rectangle)
            self.screen.blit(label, rectangle)
