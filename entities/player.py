import pygame

from entities.base_entity import BaseEntity
from config import Config


class Player(BaseEntity):

    def add_abc(self, abc):
        abc = abc + 1
        return abc

    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.image = pygame.transform.scale(self.image, (Config.PLAYER_WIDTH, Config.PLAYER_HEIGHT))
