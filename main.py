import sys
import pygame


class Game:

    def __init__(self):
        # initialize and create game resource
        pygame.init()

        """
        set the screen for display
        set_mode get the size 
        set_caption get the name
        """
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Aliens Invasion')

    def run_game(self):
        while True:
            # keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    # launch game
    game = Game()
    game.run_game()
