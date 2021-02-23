import sys
import pygame
from Settings import Settings


class Game:

    def __init__(self):
        # initialize and create game resource
        pygame.init()

        self.settings = Settings()
        """
        set the screen for display
        set_mode create window
        set_caption add the name
        screen.fill set the bg color
        """
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption('Aliens Invasion')

    def run_game(self):
        while True:
            # keyboard and mouse event
            for event in pygame.event.get():
                # to close the game
                if event.type == pygame.QUIT:
                    sys.exit()

            # update all screen
            pygame.display.flip()


if __name__ == '__main__':
    # launch game
    game = Game()
    game.run_game()
