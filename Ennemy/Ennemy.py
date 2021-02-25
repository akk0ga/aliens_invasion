import pygame
from pygame.sprite import Sprite


class Ennemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('assets/ennemy/weak.bmp')
        self.rect = self.image.get_rect()
        self.group = pygame.sprite.Group()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def create(self, game):
        max_ennemies = (game.settings.screen_width - (2 * self.rect.width)) // (2 * self.rect.width)
        print(max_ennemies)
        for i in range(max_ennemies):
            ennemy = Ennemy(game)
            ennemy.x = ennemy.rect.width + 2 * ennemy.rect.width * i
            ennemy.rect.x = ennemy.x
            self.group.add(ennemy)
