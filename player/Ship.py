import pygame


class Ship:

    def __init__(self, game):
        # initialize ship and set start position
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # load image
        self.image = pygame.image.load('assets/player.bmp')
        self.rect = self.image.get_rect()

        # start ship middle bottom screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
