import pygame
from ..components.component import Component

class Breadboard:
    components: list[Component]
    
    def __init__(self, surface, top):
        self.top = top
        self.screen = surface
        self.image = pygame.image.load('./simulator/breadboard/breadboard.png').convert()
        self.components = []

    def add(self, component: Component):
        self.components.append(component)

    def draw(self):
        # draw the board
        left = (self.screen.get_width() / 2) - (self.image.get_rect().width / 2)
        rect = (left, self.top, self.image.get_rect().width, self.image.get_rect().height)
        self.screen.blit(self.image, rect)

        # draw the components
        for component in self.components:
            component.draw(self.screen)