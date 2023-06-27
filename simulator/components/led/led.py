import pygame
from ..component import Component 

class Led(Component):
    def __init__(self, pin_no, x, y):
        self.pin_no = pin_no
        self.x = x
        self.y = y
        self.image = pygame.image.load('./simulator/components/led/led_off.png').convert_alpha()

    def draw(self, surface):
        rect = (self.x, self.y, self.image.get_rect().width, self.image.get_rect().height)
        surface.blit(self.image, rect)