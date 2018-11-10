import pygame
from game import Game


def main():
    pygame.init()
    pygame.display.set_caption("typing RPG")

    game = Game()

    running = True
    while running:
        events = pygame.event.get()
        game.tick(events)
        game.draw()
        pygame.display.flip()
        for event in events:
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
