import pygame
from pygame.sprite import Sprite
from random import randint


class Ennemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.enemy = self._choose_ennemy()
        self.image = pygame.image.load(f'assets/ennemy/{self.enemy["image"]}.bmp')
        self.rect = self.image.get_rect()
        self.screen = game.screen.get_rect()
        self.speed = 1.0
        self.life = self.enemy["life"]

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = self.speed

    def _choose_ennemy(self):
        image = ('weak', 'medium', 'strong')
        random = randint(0, 2)
        life = 1

        if random == 1:
            life = 3
        elif random == 2:
            life = 6

        result = {
            'image': image[random],
            'life': life
        }
        return result

    def update(self, game, move: bool):
        if move:
            self.x += (self.speed * game.settings.enemy_direction)
            self.rect.x += self.x
            self.x = 0
        else:
            self.life -= 1
            print(self.life)
            return self.life
