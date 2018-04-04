import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.surf = pygame.Surface((50,50))
       self.surf.fill((255,255,255))
       self.rect = self.surf.get_rect()
       self.rect.center = (0,0)

    def move(self,pressed_keys):
        if pressed_keys == pygame.K_UP:
            self.rect.move_ip(0,-5)
        if pressed_keys == pygame.K_DOWN:
            self.rect.move_ip(0,5)
        if pressed_keys == pygame.K_LEFT:
            self.rect.move_ip(-5,0)
        if pressed_keys == pygame.K_RIGHT:
            self.rect.move_ip(5,0)

    def getCoordinates(self):
        return self.rect.center
