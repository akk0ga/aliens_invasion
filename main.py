import sys
import pygame

from aliens_invasion.settings.Settings import Settings
from player.Ship import Ship
from aliens_invasion.ennemy.Fleet import Fleet


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
        pygame.display.set_caption('Aliens Invasion')

        # initialize player
        self.ship = Ship(self, self.settings)

        # initialize ennemy
        self.fleet = Fleet()
        self.enemies = self.fleet.enemies
        self.fleet.create_fleet(self)

    def _control(self):
        # keyboard and mouse event
        for event in pygame.event.get():
            # close the game
            if event.type == pygame.QUIT:
                sys.exit()
            if self.enemies:
                self.ship.move(event)
                self.ship.attack(event, self)

    def _update_screen(self):
        self.screen.blit(self.settings.background, (0, 0))
        # display player
        self.ship.blit_ship()

        # ennemy
        self.enemies.draw(self.screen)

        # update bullets
        for bullet in self.ship.bullets.sprites():
            bullet.display()

        # .copy() copy the original because for loop has to get the same lenght during all the loop
        # group collide delete sprite ennemy and bullet
        for bullet in self.ship.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.ship.bullets.remove(bullet)

            sprites_collided = pygame.sprite.groupcollide(self.ship.bullets, self.enemies, False, False)
            for bullet, enemy in sprites_collided.items():
                bullet.remove(self.ship.bullets)


        # update enemies direction
        for enemy in self.enemies.sprites():
            if enemy.rect.right == self.screen.get_rect().right:
                self.settings.enemy_direction = -1
            elif enemy.rect.left == self.screen.get_rect().left:
                self.settings.enemy_direction = 1

        # update all screen
        pygame.display.flip()

    def _run_game(self):
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            self._control()
            self._update_screen()
            if self.settings.game_active:
                self.enemies.update(self, True)
                self.ship.bullets.update()
                self.ship.update_movement()
                if not self.enemies:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('assets/sound/bg/Victory.wav')
                    pygame.mixer.music.play()
                    self.settings.game_active = False
                    self.ship.rect.midbottom = self.screen.get_rect().midbottom
            clock.tick(110)


if __name__ == '__main__':
    # launch game
    game = AlienInvasion()
    game._run_game()
