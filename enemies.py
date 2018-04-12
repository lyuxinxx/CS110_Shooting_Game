import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400

class Enemy(pygame.sprite.Sprite):
    """
        This class represents the enermy.
    """
    def __init__(self, speed):
        """
            Initiate enemies.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image\\lander.png")
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = random.randrange(screen_height - self.image.get_height())
        self.speed = speed
        
    def update(self):
        """
            Update the enermies' position.
        """
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
