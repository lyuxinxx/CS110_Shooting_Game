import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400

class Player(pygame.sprite.Sprite):
    """
        This class represents the Player.
    """
    def __init__(self):
        """
            Initiate the player.
        """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image\\space-shuttle-1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200
        self.x_speed = 0
        self.y_speed = 0
        
    def update(self):
        """
            Update the player's position.
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
        if self.rect.x > screen_width:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = screen_height
        if self.rect.y > screen_height:
            self.rect.y = 0
