import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
            ):  # pygame.QUIT => user clicked X to close the window
                running = False

        screen.fill("black")
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
