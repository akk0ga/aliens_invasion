import pygame
from pygame.sprite import Sprite
from random import randint


class Ennemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load(f'assets/ennemy/{self.choose_ennemy()}.bmp')
        self.rect = self.image.get_rect()
        self.speed = 1.0

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = 0

    def choose_ennemy(self):
        image = ('weak', 'medium', 'strong')
        return image[randint(0, 2)]

    def update(self):
        self.x = self.speed
        self.x += self.speed
        self.rect.x += self.x
