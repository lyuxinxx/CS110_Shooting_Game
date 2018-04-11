import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400

class Rock(pygame.sprite.Sprite):
    """
        This class represents the rocks.
    """
    def __init__(self):
        """
            Initiate the rocks.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image\\comet.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = random.randrange(screen_height)

    def update(self, speed):
        """
            Update the rocks' position.
        """
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()
