import pygame
import random

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
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.image.set_colorkey((255,255,255))
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
