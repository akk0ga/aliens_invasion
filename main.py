import sys
import pygame

from Settings import Settings
from player.Ship import Ship


class AlienInvasion:

    def __init__(self):
        # initialize and create game resource
        pygame.init()

        self.settings = Settings(self)
        """
        set the screen for display
        set_mode create window
        set_caption add the name
        screen.fill set the bg color
        """
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Aliens Invasion')

        # initialize player ship
        self.ship = Ship(self, self.settings)

    def control(self):
        # keyboard and mouse event
        for event in pygame.event.get():
            # close the game
            if event.type == pygame.QUIT:
                sys.exit()
            self.ship.move(event)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # display player
        self.ship.blit_ship()
        # update all screen
        pygame.display.flip()

    def run_game(self):
        while True:
            self.control()
            self.ship.update_movement()
            self.update_screen()


if __name__ == '__main__':
    # launch game
    game = AlienInvasion()
    game.run_game()
