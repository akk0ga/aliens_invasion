import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 0.2
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 3

        self.screen = game.screen
        self.settings = game.settings

        # create bullet sprite
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # set position y
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y

    def display(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
