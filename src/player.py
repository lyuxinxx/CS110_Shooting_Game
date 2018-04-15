import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400
init_x = 0
init_y = 200

class Player(pygame.sprite.Sprite):
    """
        This class represents the Player.
    """
    def __init__(self):
        """
            Initiate the player.
        """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets\\space-shuttle-1.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = init_x 
        self.rect.y = init_y
        self.x_speed = 0
        self.y_speed = 0
        
    def update(self):
        """
            Update the player's position.
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
        if self.rect.right > screen_width:
            self.rect.right = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


    
