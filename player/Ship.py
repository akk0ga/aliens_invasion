import pygame


class Ship:

    def __init__(self, game, settings):
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
        self.ship_speed = 0.3

        self.x = float(self.rect.x)

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
