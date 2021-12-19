import sys
import random
import pygame

from entities.player import Player
from entities.enemy import Enemy
from entities.bullet import Bullet
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
        self.background = pygame.image.load(r'data/images/background.png').convert()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))
        self.game_over_font = pygame.font.Font(r'data/fonts/04B_19.TTF', 36)
        self.score_font = pygame.font.Font(r'data/fonts/04B_19.TTF', 24)

        self.clock = pygame.time.Clock()

        self.player = self.__create_player()

        # Init 5 enemies
        self.enemies = []
        for i in range(5):
            enemy = self.__create_enemy()
            self.enemies.append(enemy)

        # Init bullets
        self.bullets = []

        # Set: sau 1s, su kien USEREVENT se xay ra
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.is_game_over = False
        self.score = 0

    @staticmethod
    def __create_player():
        # Tao nhan vat player
        x = Config.WIDTH // 2 - Config.PLAYER_WIDTH // 2
        y = Config.HEIGHT - 120
        player = Player(r'data/images/player.png', x=x, y=y, move_step=3)

        return player

    @staticmethod
    def __create_enemy():
        x = random.randint(0, Config.WIDTH - Config.ENEMY_WIDTH)
        y = random.randint(0, 200)
        enemy = Enemy(r'data/images/enemy.png', x, y, move_step=3, orient=Config.LEFT)

        return enemy

    def __check_quit_game(self, events):
        # Check xem co tat game hay khong
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def __move_entities(self):
        # Di chuyen cac nhan vat va dan
        self.player.move()  # cap nhat x, y neu chung ta nhan phim
        for enemy in self.enemies:
            enemy.move()  # cap nhat x, y cua enemy tuy thuoc vao huong cua no
        for bullet in self.bullets:
            bullet.move()

    def __add_enemy(self, events):
        for event in events:
            if event.type == pygame.USEREVENT:
                enemy = self.__create_enemy()
                self.enemies.append(enemy)

    def __add_bullet(self):
        # add new bullet
        bullet = self.player.fire()
        if bullet is not None:
            self.bullets.append(bullet)

    def __check_collision(self):
        # Kiem tra dan co cham enemy
        for bullet in self.bullets:
            for enemy in self.enemies:
                if enemy.available and bullet.collision(enemy):
                    bullet.available = False
                    enemy.available = False
                    self.score += 1
                    break

        # Neu enemy cham vao player => game over
        for enemy in self.enemies:
            if enemy.available and enemy.collision(self.player):
                self.is_game_over = True

    def __remove_unavailable_entities(self):
        new_enemies = []
        for enemy in self.enemies:
            if enemy.available:
                new_enemies.append(enemy)
        self.enemies = new_enemies

        new_bullets = []
        for bullet in self.bullets:
            if bullet.available:
                new_bullets.append(bullet)
        self.bullets = new_bullets

    def __draw_game_state(self):
        # Ve trang thai hien tai cua game
        # Draw background
        self.screen.blit(self.background, (0, 0))

        # Draw player
        self.screen.blit(self.player.image, (self.player.x, self.player.y))

        # Draw enemy
        for enemy in self.enemies:
            self.screen.blit(enemy.image, (enemy.x, enemy.y))

        # Draw bullet
        for bullet in self.bullets:
            self.screen.blit(bullet.image, (bullet.x, bullet.y))

        # Draw score
        text = self.score_font.render('Score: {}'.format(self.score), True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # Update screen
        pygame.display.update()

    def __draw_game_over_state(self):
        # Draw background
        self.screen.blit(self.background, (0, 0))

        text = self.game_over_font.render('GAME OVER', True, (255, 255, 255))
        width = text.get_width()
        height = text.get_height()
        x = Config.WIDTH / 2 - width / 2
        y = Config.HEIGHT / 2 - height / 2
        self.screen.blit(text, (x, y))

        # Update screen
        pygame.display.update()

    def run(self):  # Run game
        while True:
            events = pygame.event.get()
            self.__check_quit_game(events)

            if not self.is_game_over:
                self.__move_entities()
                self.__add_enemy(events)
                self.__add_bullet()
                self.__check_collision()
                self.__remove_unavailable_entities()
                self.__draw_game_state()

            else:
                self.__draw_game_over_state()

            self.clock.tick(120)  # => 120 frame per second
