import sys
import pygame


class Game:

    def __init__(self):
        # initialize and create game resource
        pygame.init()

        """
        set the screen for display
        set_mode create window
        set_caption add the name
        screen.fill set the bg color
        """
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (222, 219, 210)
        self.screen.fill(self.bg_color)
        pygame.display.set_caption('Aliens Invasion')

    def run_game(self):
        while True:
            # keyboard and mouse event
            for event in pygame.event.get():
                # to close the game
                if event.type == pygame.QUIT:
                    sys.exit()

            # update all screen
            pygame.display.flip()


if __name__ == '__main__':
    # launch game
    game = Game()
    game.run_game()
