import pygame
import gradients


class Renderer:
    # SIZES
    WINDOW_WIDTH = 480
    WINDOW_HEIGHT = 640
    WORDS_MARGIN_TOP = 90
    TIME_TO_HIT_MARGIN_TOP = 60
    BAR_MARGIN = 10
    BAR_BORDER_WIDTH = 2
    HEALTH_BAR_HEIGHT = 40
    EXPERIENCE_BAR_HEIGHT = 20
    EXPERIENCE_HEALTH_BAR_PADDING = 5
    HIT_HEALTH_BAR_PADDING = 5
    HIT_BAR_HEIGHT = 20

    # COLORS
    WORD_COLOR = (52, 52, 52)
    BACKGROUND_COLOR = (56, 119, 119)
    WORD_HIGHLIGHT_COLOR = (153, 179, 179)
    HEALTH_BAR_COLOR = (255, 0, 0)
    HEALTH_BAR_BACKGROUND_COLOR = (50, 50, 50)
    EXPERIENCE_BAR_COLOR = (255, 165, 0)
    EXPERIENCE_BAR_BACKGROUND_COLOR = (50, 50, 50)
    HIT_BAR_COLOR = (100, 200, 200)
    HIT_BAR_BACKGROUND_COLOR = (50, 50, 50)
    ENEMY_NAME_TEXT_COLOR = (200, 200, 200)

    # FONTS
    DEFAULT_FONT_BOLD = 'Inconsolata-Bold.ttf'
    DEFAULT_FONT_REGULAR = 'Inconsolata-Regular.ttf'
    WORD_FONT_SIZE = 32

    # WIN AND LOSS SCREEN
    WIN_BACKGROUND_COLOR = (210, 210, 210)
    WIN_TEXT_COLOR = (50, 50, 50)
    WIN_TEXT = "You win! :)"
    LOSS_BACKGROUND_COLOR = (35, 35, 35)
    LOSS_TEXT_COLOR = (255, 0, 0)
    LOSS_TEXT = "You died! :("

    def __init__(self):
        self.screen = pygame.display.set_mode((Renderer.WINDOW_WIDTH, Renderer.WINDOW_HEIGHT))
        self.font = pygame.font.Font(Renderer.DEFAULT_FONT_BOLD, Renderer.WORD_FONT_SIZE)
        self.width, self.height = pygame.display.get_surface().get_size()

    def text_objects(self, text, color, text_center):
        rendered = self.font.render(text, True, color)
        return rendered, rendered.get_rect(center=text_center)

    def draw_background(self):
        self.screen.fill(Renderer.BACKGROUND_COLOR)

    def render_time_bar(self, max_time, current_time):
        background, foreground = self.create_bar(
            0,
            Renderer.HIT_HEALTH_BAR_PADDING + Renderer.HEALTH_BAR_HEIGHT,
            Renderer.HIT_BAR_HEIGHT,
            current_time / max_time
        )
        pygame.draw.rect(self.screen, Renderer.HIT_BAR_BACKGROUND_COLOR, background)
        pygame.draw.rect(self.screen, Renderer.HIT_BAR_COLOR, foreground)

    def render_player_health_bar(self, max_health, current_health):
        background, foreground = self.create_bar(
            0,
            self.height - Renderer.HEALTH_BAR_HEIGHT - 2 * Renderer.BAR_MARGIN - Renderer.EXPERIENCE_BAR_HEIGHT - Renderer.EXPERIENCE_HEALTH_BAR_PADDING,
            Renderer.HEALTH_BAR_HEIGHT,
            current_health / max_health
        )
        pygame.draw.rect(self.screen, Renderer.HEALTH_BAR_BACKGROUND_COLOR, background)
        pygame.draw.rect(self.screen, Renderer.HEALTH_BAR_COLOR, foreground)

    def render_enemy_health_bar(self, max_health, current_health, name):
        background, foreground = self.create_bar(
            0,
            0,
            Renderer.HEALTH_BAR_HEIGHT,
            current_health / max_health
        )
        pygame.draw.rect(self.screen, Renderer.HEALTH_BAR_BACKGROUND_COLOR, background)
        pygame.draw.rect(self.screen, Renderer.HEALTH_BAR_COLOR, foreground)

        label, rectangle = self.text_objects(
            name,
            Renderer.ENEMY_NAME_TEXT_COLOR,
            (self.width / 2, Renderer.HEALTH_BAR_HEIGHT / 2 + Renderer.BAR_MARGIN)
        )
        self.screen.blit(label, rectangle)

    def render_experience_bar(self, max_experience, current_experience):
        background, foreground = self.create_bar(
            0,
            self.height - Renderer.EXPERIENCE_BAR_HEIGHT - 2 * Renderer.BAR_MARGIN,
            Renderer.EXPERIENCE_BAR_HEIGHT,
            current_experience / max_experience
        )
        pygame.draw.rect(self.screen, Renderer.EXPERIENCE_BAR_BACKGROUND_COLOR, background)
        pygame.draw.rect(self.screen, Renderer.EXPERIENCE_BAR_COLOR, foreground)

    def draw_gradient(self, rectangle, from_color, to_color):
        self.screen.blit(gradients.vertical((rectangle.width, rectangle.height), from_color, to_color), (rectangle.left, rectangle.top))

    def render_words(self, words, valid_words, current_letter_count):
        for i in range(len(words)):
            top = i * Renderer.WORD_FONT_SIZE + Renderer.WORDS_MARGIN_TOP
            label, rectangle = self.text_objects(
                words[i].word.upper(),
                Renderer.WORD_COLOR,
                (self.width / 2, top + Renderer.WORD_FONT_SIZE / 2)
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

    def create_bar(self, x, y, height, percentage):
        health_bar_background_width = self.width - 2 * Renderer.BAR_MARGIN
        health_bar_width = (health_bar_background_width - 2 * Renderer.BAR_BORDER_WIDTH) * percentage

        health_bar_background = pygame.Rect(
            x + Renderer.BAR_MARGIN,
            y + Renderer.BAR_MARGIN,
            health_bar_background_width,
            height
        )
        health_bar = pygame.Rect(
            x + Renderer.BAR_MARGIN + Renderer.BAR_BORDER_WIDTH,
            y + Renderer.BAR_MARGIN + Renderer.BAR_BORDER_WIDTH,
            health_bar_width,
            height - 2 * Renderer.BAR_BORDER_WIDTH
        )

        return health_bar_background, health_bar

    def render_win_screen(self):
        self.screen.fill(Renderer.WIN_BACKGROUND_COLOR)
        label, rectangle = self.text_objects(
            Renderer.WIN_TEXT,
            Renderer.WIN_TEXT_COLOR,
            (self.width / 2, self.height / 2)
        )
        self.screen.blit(label, rectangle)

    def render_loss_screen(self):
        self.screen.fill(Renderer.LOSS_BACKGROUND_COLOR)
        label, rectangle = self.text_objects(
            Renderer.LOSS_TEXT,
            Renderer.LOSS_TEXT_COLOR,
            (self.width / 2, self.height / 2)
        )
        self.screen.blit(label, rectangle)
