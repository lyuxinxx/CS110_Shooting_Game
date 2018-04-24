import pygame
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400

class HelpMenu:
    """
        This class represents the Help Menu.
    """
    def __init__(self):
        """
            Initiate the Help Menu.
        """
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.bg_image = pygame.image.load("assets\\HelpMenu.png").convert()
        pygame.display.set_caption("Help Menu")
        self.font = pygame.font.SysFont("font",30)

        self.screen.blit(self.bg_image,(0,0))
        pygame.display.flip()
        time.sleep(5)
