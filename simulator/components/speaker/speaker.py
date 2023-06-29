# <a href="https://www.flaticon.com/free-icons/speaker" title="speaker icons">Speaker icons created by Freepik - Flaticon</a>

import pygame
from .note import Note
from ..component import Component 

class Speaker(Component):
    def __init__(self, pin_no, x, y):
        self.pin = pin_no
        self.x = x
        self.y = y
        self.image = pygame.image.load('./simulator/components/led/led_on.png').convert_alpha()
        self.note = None

    def draw(self, surface):
        rect = (self.x, self.y, self.image.get_rect().width, self.image.get_rect().height)
        surface.blit(self.image, rect)

    def digital_write(self, pin: int, value: str):
        # sample speaker value: cmd={tone_command}&frequency={frequency}&duration={duration}
        parts = value.split('&')

        for part in parts:
            if part.find("cmd") > -1:
                cmd = part.replace("cmd=", "")
            elif part.find("frequency=", "") > -1:
                frequency = part.replace("frequency=")
            elif part.find("duration") > -1:
                duration = part.replace("duration=", "")

        if cmd == 0:
            if self.note is None:
                self.note = Note(int(frequency))

            self.note.play()
        elif cmd == 1:
            if self.note is not None:
                self.note.stop()