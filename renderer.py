import pygame
import gradients


class Renderer:
    # SIZES
    WINDOW_WIDTH = 480
    WINDOW_HEIGHT = 640
    WORDS_MARGIN_TOP = 60
    HEALTH_BAR_MARGIN = 10
    HEALTH_BAR_HEIGHT = 40
    HEALTH_BAR_BORDER_WIDTH = 2

    # COLORS
    WORD_COLOR = (52, 52, 52)
    BACKGROUND_COLOR = (56, 119, 119)
    WORD_HIGHLIGHT_COLOR = (153, 179, 179)
    HEALTH_BAR_COLOR = (255, 0, 0)
    HEALTH_BAR_BACKGROUND_COLOR = (50, 50, 50)

    # FONTS
    DEFAULT_FONT_BOLD = 'Inconsolata-Bold.ttf'
    DEFAULT_FONT_REGULAR = 'Inconsolata-Regular.ttf'
    WORD_FONT_SIZE = 32

    def __init__(self):
        self.screen = pygame.display.set_mode((Renderer.WINDOW_WIDTH, Renderer.WINDOW_HEIGHT))
        self.font = pygame.font.Font(Renderer.DEFAULT_FONT_BOLD, Renderer.WORD_FONT_SIZE)
        self.width, self.height = pygame.display.get_surface().get_size()

    def text_objects(self, text, color, text_center):
        rendered = self.font.render(text, True, color)
        return rendered, rendered.get_rect(center=text_center)

    def draw_background(self):
        self.screen.fill(Renderer.BACKGROUND_COLOR)

    def render_player_health_bar(self, max_health, current_health):
        # TODO: Move
        health_bar_background_width = self.width - 2 * Renderer.HEALTH_BAR_MARGIN
        health_bar_width = (health_bar_background_width - 2 * Renderer.HEALTH_BAR_BORDER_WIDTH) * current_health / max_health

        health_bar_background = pygame.Rect(
            Renderer.HEALTH_BAR_MARGIN,
            Renderer.HEALTH_BAR_MARGIN,
            health_bar_background_width,
            Renderer.HEALTH_BAR_HEIGHT
        )
        health_bar = pygame.Rect(
            Renderer.HEALTH_BAR_MARGIN + Renderer.HEALTH_BAR_BORDER_WIDTH,
            Renderer.HEALTH_BAR_MARGIN + Renderer.HEALTH_BAR_BORDER_WIDTH,
            health_bar_width,
            Renderer.HEALTH_BAR_HEIGHT - 2 * Renderer.HEALTH_BAR_BORDER_WIDTH
        )

        pygame.draw.rect(self.screen, Renderer.HEALTH_BAR_BACKGROUND_COLOR, health_bar_background)
        pygame.draw.rect(self.screen, Renderer.HEALTH_BAR_COLOR, health_bar)

    def draw_gradient(self, rectangle, from_color, to_color):
        self.screen.blit( gradients.vertical((rectangle.width, rectangle.height), from_color, to_color),(rectangle.left,rectangle.top))

    def render_words(self, words, valid_words, current_letter_count):
        for i in range(len(words)):
            top = i * Renderer.WORD_FONT_SIZE + Renderer.WORDS_MARGIN_TOP
            label, rectangle = self.text_objects(
                words[i].word.upper(),
                Renderer.WORD_COLOR,
                (
                    self.width / 2,
                    top + Renderer.WORD_FONT_SIZE / 2
                )
            )

            if words[i] in valid_words and current_letter_count > 0:
                count_of_letters = len(words[i].word)
                new_rectangle = pygame.Rect(
                    rectangle.left,
                    rectangle.top,
                    rectangle.width * (current_letter_count / count_of_letters),
                    rectangle.height
                )
                pygame.draw.rect(self.screen, Renderer.WORD_HIGHLIGHT_COLOR, new_rectangle)

            self.screen.blit(label, rectangle)
