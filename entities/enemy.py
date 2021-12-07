import pygame

from entities.base_entity import BaseEntity
from config import Config


class Enemy(BaseEntity):

    def __init__(self, image_path, x, y, move_step):
        super().__init__(image_path, x, y, move_step)
        self.image = pygame.transform.scale(self.image, (Config.ENEMY_WIDTH, Config.ENEMY_HEIGHT))
