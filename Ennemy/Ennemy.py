import pygame
import random
from pygame.sprite import  Sprite


class Ennemy(Sprite):

    def __init__(self, game):
        super().__init__()
        self.ennemy = pygame.image.load(f'assets/{self.ennemy_choice()}.bmp')
        self.ennemy_rect = self.ennemy.get_rect()
        

    def ennemy_choice(self):
        ennemy_list = {
            1: 'weak',
            2: 'medium',
            3: 'strong'
        }
        ennemy = random.randint(1, 3)
        return ennemy_list[ennemy]
