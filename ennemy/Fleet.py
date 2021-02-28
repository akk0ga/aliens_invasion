import pygame
from aliens_invasion.ennemy.Ennemy import Ennemy
from pygame.sprite import Sprite
from aliens_invasion.settings.Settings import Settings


class Fleet(Sprite):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.enemies = pygame.sprite.Group()

    def create_fleet(self, game):
        enemy = Ennemy(game)
        enemy_width, enemy_height = enemy.rect.size

        available_space_x = self.settings.screen_width - (2 * enemy_width) - game.ship.rect.height
        total_lines = available_space_x // (2 * enemy_width)

        available_space_y = self.settings.screen_height - (3 * enemy_height)
        total_rows = available_space_y // (2 * enemy_height)

        for row in range(total_rows):
            for line in range(total_lines):
                self.__create_enemy(line, row, game)

    def __create_enemy(self, line, row, game):
        enemy = Ennemy(game)
        enemy_width = enemy.rect.width

        enemy.rect.x = enemy_width + 2 * enemy_width * line
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row

        self.enemies.add(enemy)
