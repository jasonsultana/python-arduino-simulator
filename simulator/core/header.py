import pygame
from pygame.locals import *
from .colours import Colours
from .label import Label

class Header:
    def __init__(self, screen):
        self.screen = screen
        self.lbl_position = Label(screen, 'freesansbold.ttf', 16)
        self.lbl_position.set_colour(Colours.WHITE).set_background_colour(Colours.BLACK)
        self.lbl_position.set_center(self.screen.get_width() / 8, 25)
        self.lbl_position.set_text('')
        self.lbl_position.set_default('')

        self.lbl_title = Label(screen, 'freesansbold.ttf', 16)
        self.lbl_title.set_colour(Colours.WHITE).set_background_colour(Colours.BLACK)
        self.lbl_title.set_center(self.screen.get_width() / 2, 25)
        self.lbl_title.set_text('N/A')
        self.lbl_title.set_default('N/A')

    def set_mouse_pos(self, x, y):
        self.lbl_position.set_text(f"x: {x}, y: {y}")

    def set_title(self, title):
        self.lbl_title.set_text(title)

    def draw(self):
        self.lbl_position.draw()
        self.lbl_title.draw()