import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class MenuItem(pygame.font.Font):
    """
        This class represents the menu item.
    """
    def __init__(self, text, font = None, font_size = 30,
                 font_color=WHITE, xy=(0, 0)):
        """
            Initiate the menu item.
        """
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x, self.pos_y = xy
        self.position = xy

    def is_mouse_selection(self, xy):
        '''
           Look for mouse position.
        '''
        posx, posy = xy
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False

    def set_position(self, x, y):
        '''
           Set up mouse position.
        '''
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        '''
           Set up the font color of the menu item.
        '''
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
