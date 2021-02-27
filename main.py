import sys
import pygame

from Settings import Settings
from player.Ship import Ship
from aliens_invasion.ennemy.Ennemy import Ennemy


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

        # initialize player
        self.ship = Ship(self, self.settings)

        # initialize ennemy
        self.ennemies = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        ennemy = Ennemy(self)
        ennemy_width, ennemy_height = ennemy.rect.size

        available_space_x = self.settings.screen_width - (2 * ennemy_width) - self.ship.rect.height
        total_lines = available_space_x // (2 * ennemy_width)

        available_space_y = self.settings.screen_height - (3 * ennemy_height)
        total_rows = available_space_y // (2 * ennemy_height)

        for row in range(total_rows):
            for line in range(total_lines):
                self._create_ennemy(line, row)

    def _create_ennemy(self, line, row):
        ennemy = Ennemy(self)
        ennemy_width = ennemy.rect.width

        ennemy.rect.x = ennemy_width + 2 * ennemy_width * line
        ennemy.rect.y = ennemy.rect.height + 2 * ennemy.rect.height * row

        self.ennemies.add(ennemy)

    def _update_ennemy(self):
        self.ennemies.update()

    def _control(self):
        # keyboard and mouse event
        for event in pygame.event.get():
            # close the game
            if event.type == pygame.QUIT:
                sys.exit()
            self.ship.move(event)
            self.ship.attack(event, self)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # display player
        self.ship.blit_ship()

        # ennemy
        self.ennemies.draw(self.screen)

        # update bullets
        for bullet in self.ship.bullets.sprites():
            bullet.display()

        # .copy() copy the original because for loop has to get the same lenght during all the loop
        for bullet in self.ship.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.ship.bullets.remove(bullet)

        # update all screen
        pygame.display.flip()

    def _run_game(self):
        clock = pygame.time.Clock()
        while True:
            self._control()
            self.ship.update_movement()
            self.ship.bullets.update()
            self._update_ennemy()
            self._update_screen()
            clock.tick(120)


if __name__ == '__main__':
    # launch game
    game = AlienInvasion()
    game._run_game()
