import pygame

screen_width = 700
screen_height = 400

class Bullet(pygame.sprite.Sprite):
    """
        This class represents the bullet.
    """
    def __init__(self,x,y):
        """
            Initiate the bullet.
        """
        super().__init__()

        self.image = pygame.Surface((8,4))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        """
            Move the bullets.
        """
        self.rect.x += 10 
        if self.rect.right > screen_width:
            self.kill()
