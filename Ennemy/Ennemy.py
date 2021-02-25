import pygame
from pygame.sprite import Sprite


class Ennemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load('assets/ennemy/weak.bmp')
        self.rect = self.image.get_rect()
        self.group = pygame.sprite.Group()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def create(self, game):
        ennemy = Ennemy(game)
        self.group.add(ennemy)
