import pygame

from entities.base_entity import BaseEntity
from entities.bullet import Bullet
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

    def fire(self):
        # Tao ra vien dan o dau player
        x = self.x + Config.PLAYER_WIDTH // 2 - Config.BULLET_WIDTH // 2
        y = self.y - Config.BULLET_HEIGHT

        bullet = Bullet(r'data/images/bullet.png', x, y, move_step=3)

        return bullet
