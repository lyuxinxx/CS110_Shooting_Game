import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400

class Bullet(pygame.sprite.Sprite):
    """
        This class represents the bullet.
    """
    def __init__(self,x,y,width = 8, height = 4):
        """
            Initiate the bullet.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image\\rocket-ship-1.png").convert()
        self.image.set_colorkey(BLACK)
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
