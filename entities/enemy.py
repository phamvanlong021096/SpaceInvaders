import pygame

from entities.base_entity import BaseEntity
from config import Config


class Enemy(BaseEntity):

    def __init__(self, image_path, x, y, move_step, orient):
        super().__init__(image_path, x, y, move_step)
        self.image = pygame.transform.scale(self.image, (Config.ENEMY_WIDTH, Config.ENEMY_HEIGHT))
        self.orient = orient

    def move(self):
        if self.orient == Config.LEFT:
            self.x -= self.move_step

        if self.orient == Config.RIGHT:
            self.x += self.move_step

        if self.x < 0:
            self.x = 0
            self.y += 75
            self.orient = Config.RIGHT

        if self.x > Config.WIDTH - Config.ENEMY_WIDTH:
            self.x = Config.WIDTH - Config.ENEMY_WIDTH
            self.y += 75
            self.orient = Config.LEFT

        # Check xem enemy co di ra ngoai cua so gam hay khong
        if self.y > Config.HEIGHT:
            self.available = False
