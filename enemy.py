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
    def __init__(self):
        """
            Initiate enemies.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image\\lander.png")
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = random.randrange(screen_height)
        
    def update(self,speed):
        """
            Update the enermies' position.
        """
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()
