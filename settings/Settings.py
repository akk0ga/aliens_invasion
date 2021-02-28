import pygame
import sys

from player.Ship import Ship


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (222, 219, 210)
        self.enemy_direction = 1
        self.game_active = True
