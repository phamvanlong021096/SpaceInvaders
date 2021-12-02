import pygame

from game_controller import GameController


def main():
    # Khoi tao thanh phan pygame
    pygame.init()

    game = GameController()
    game.run()


if __name__ == '__main__':
    main()
