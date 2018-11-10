import pygame
import renderer
from game import Game


def main():
    pygame.init()
    pygame.display.set_caption("typing RPG")

    screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
    game = Game()

    running = True
    while running:
        game.draw(screen)
        # game.tick()
        # renderer.render_all(game, screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                game.handle_key(event.key)
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
