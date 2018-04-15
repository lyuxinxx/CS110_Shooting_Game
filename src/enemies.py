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
    def __init__(self, speed = 3):
        """
            Initiate enemies.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets\\lander.png")
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = random.randrange(screen_height - self.image.get_height())
        self.x_speed = speed / 2
        self.y_speed = random.sample([-speed, speed],k=1)[0]
        
    def update(self):
        """
            Update the enermies' position.
        """
        self.rect.x -= self.x_speed
        self.rect.y += self.y_speed
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.y_speed = - self.y_speed
        if self.rect.x < 0:
            self.kill()
