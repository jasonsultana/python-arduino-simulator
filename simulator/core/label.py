import pygame
from pygame.locals import *

class Label:
    def __init__(self, surface, font_name, font_size):
        self.surface = surface
        self.font_name = font_name
        self.font_size = font_size
        self.font = pygame.font.Font(font_name, font_size)

    def set_colour(self, colour):
        self.colour = colour
        return self
    
    def set_background_colour(self, background_colour):
        self.background_colour = background_colour
        return self

    def set_center(self, x, y):
        self.center = (x, y)
        return self
    
    def set_default(self, default_text):
        self.default_text = default_text
        return self
    
    def set_text(self, text):
        self.text = text
        return self
    
    def draw(self):
        # render(text, antialias, color, background=None) -> Surface
        result = self.font.render(self.text, True, self.colour, self.background_colour)
        rect = result.get_rect()
        rect.center = self.center

        self.surface.blit(result, rect)

