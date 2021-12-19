import pygame


# Class truu tuong/ cha
class BaseEntity:

    def __init__(self, image_path, x, y, move_step):
        self.image = pygame.image.load(image_path).convert_alpha()  # tao ra surface nhe
        self.x = x
        self.y = y
        self.move_step = move_step
        # available = True neu object con nam trong cua so game, nguoc lai = False
        self.available = True

    def move(self):
        pass

    def collision(self, entity):
        rect = self.image.get_rect(topleft=(self.x, self.y))
        entity_rect = entity.image.get_rect(topleft=(entity.x, entity.y))

        if rect.colliderect(entity_rect):
            return True

        return False
