import pygame
from aliens_invasion.player.Bullet import Bullet
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, game, settings):
        super().__init__()
        self.settings = settings

        # initialize ship and set start position
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # load image
        self.image = pygame.image.load('assets/player.bmp')
        self.rect = self.image.get_rect()

        # start ship middle bottom screen
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag for continuous movement
        self.move_right = False
        self.move_left = False
        self.ship_speed = 7.0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.bullets = pygame.sprite.Group()
        self.ship = pygame.sprite.Sprite()

    def blit_ship(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def update_movement(self):
        if self.move_right and self.rect.x < (self.settings.screen_width - self.image.get_width()):
            self.x += self.ship_speed

        if self.move_left and self.rect.x > 0:
            self.x -= self.ship_speed

        self.rect.x = self.x

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move ship right
                self.move_right = True
            elif event.key == pygame.K_LEFT:
                self.move_left = True
        else:
            self.move_right = False
            self.move_left = False

    def attack(self, event, game):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(self.bullets) != Bullet(game).bullet_max:
                self.settings.ship_shoot_sound.play()
                self.shoot_bullet(game)

    def shoot_bullet(self, game):
        new_bullet = Bullet(game)
        self.bullets.add(new_bullet)
