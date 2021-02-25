import pygame
from pygame.sprite import Sprite
from random import randint


class Ennemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load(f'assets/ennemy/{self.choose_ennemy()}.bmp')
        self.rect = self.image.get_rect()
        self.group = pygame.sprite.Group()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def create(self, game):
        max_ennemies = (game.settings.screen_width - (2 * self.rect.width)) // (2 * self.rect.width)
        max_rows = (game.settings.screen_height - (3 * self.rect.height) - game.ship.rect.height) // (
                    2 * self.rect.height)
        for row in range(max_rows):
            for i in range(max_ennemies):
                ennemy = Ennemy(game)
                ennemy.rect.x = ennemy.rect.width + 2 * ennemy.rect.width * i
                ennemy.rect.y = ennemy.rect.height + 2 * ennemy.rect.height * row
                self.group.add(ennemy)

    def choose_ennemy(self):
        image = ('weak', 'medium', 'strong')
        return image[randint(0, 2)]
