import sys
import pygame

from Settings import Settings
from player.Ship import Ship


class AlienInvasion:

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

        # initialize player ship
        self.ship = Ship(self)

    def events(self):
        # keyboard and mouse event
        for event in pygame.event.get():
            # to close the game
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        while True:
            # display player
            self.ship.blitme()
            self.events()
            # update all screen
            pygame.display.flip()


if __name__ == '__main__':
    # launch game
    game = AlienInvasion()
    game.run_game()
