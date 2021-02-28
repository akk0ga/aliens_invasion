import pygame


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (222, 219, 210)
        self.enemy_direction = 1
        self.game_active = True
        self.background = pygame.image.load('assets/background.bmp')
        self.ship_shoot_sound = pygame.mixer.Sound('assets/sound/effect/player_shoot.wav')
        pygame.mixer.Sound.set_volume(self.ship_shoot_sound, 0.6)
        pygame.mixer.music.load('assets/sound/bg/Venus.wav')
        pygame.mixer.music.set_volume(0.4)
