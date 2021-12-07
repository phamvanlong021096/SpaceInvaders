import pygame


# Class truu tuong/ cha
class BaseEntity:

    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y

    def move(self):
        pass
