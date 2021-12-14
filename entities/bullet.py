import pygame

from config import Config
from entities.base_entity import BaseEntity


class Bullet(BaseEntity):

    def __init__(self, image_path, x, y, move_step):
        super().__init__(image_path, x, y, move_step)
        self.image = pygame.transform.scale(self.image, (Config.BULLET_WIDTH, Config.BULLET_HEIGHT))

    def move(self):
        self.y -= self.move_step

        if self.y < -Config.BULLET_HEIGHT:
            self.available = False
