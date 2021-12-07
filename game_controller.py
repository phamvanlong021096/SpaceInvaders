import sys
import pygame

from entities.player import Player
from config import Config


# Class dieu khien game
class GameController:

    def __init__(self):
        # Set icon, caption for window screen
        icon = pygame.image.load(r'data/images/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption(Config.CAPTION)
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))

        # Load background image and scale for window screen
        self.background = pygame.image.load(r'data/images/background.png')
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))

        self.player = self.__create_player()

    @staticmethod
    def __create_player():
        # Tao nhan vat player
        x = Config.WIDTH // 2 - Config.PLAYER_WIDTH // 2
        y = Config.HEIGHT - 120
        player = Player(r'data/images/player.png', x=x, y=y, move_step=3)

        return player

    def run(self):  # Run game
        while True:
            events = pygame.event.get()  # Tra ve nhung su kien khi tuong tac voi cua so game
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.move()  # cap nhat x, y neu chung ta nhan phim

            # Draw background
            self.screen.blit(self.background, (0, 0))

            # Draw player
            self.screen.blit(self.player.image, (self.player.x, self.player.y))

            # Update screen
            pygame.display.update()
