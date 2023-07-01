import pygame
from ..component import Component 

class Led(Component):
    def __init__(self, pin_no, x, y):
        self.pin = pin_no
        self.x = x
        self.y = y
        self.off_image = pygame.image.load('./simulator/components/led/led_off.png').convert_alpha()
        self.on_image = pygame.image.load('./simulator/components/led/led_on.png').convert_alpha()

        self.image = self.off_image

    def __str__(self):
        return "Led"
    
    def digital_write(self, pin: int, value: str):
        value = int(value)
        if (value == 0):
            self.image = self.off_image
        elif (value == 1):
            self.image = self.on_image
            
    def draw(self, surface):
        rect = (self.x, self.y, self.image.get_rect().width, self.image.get_rect().height)
        surface.blit(self.image, rect)