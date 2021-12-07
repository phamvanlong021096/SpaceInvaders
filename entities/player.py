import pygame

from entities.base_entity import BaseEntity
from config import Config


class Player(BaseEntity):

    def __init__(self, image_path, x, y, move_step):
        super().__init__(image_path, x, y, move_step)
        self.image = pygame.transform.scale(self.image, (Config.PLAYER_WIDTH, Config.PLAYER_HEIGHT))

    def move(self):
        # Overwrite
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.move_step

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.move_step

        if self.x < 0:
            self.x = 0

        if self.x > Config.WIDTH - Config.PLAYER_WIDTH:
            self.x = Config.WIDTH - Config.PLAYER_WIDTH



