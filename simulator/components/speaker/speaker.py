# <a href="https://www.flaticon.com/free-icons/speaker" title="speaker icons">Speaker icons created by Freepik - Flaticon</a>

import pygame
from simulator.messages.query_string import QueryString
from .note import Note
from ..component import Component 

class Speaker(Component):
    def __init__(self, pin_no, x, y):
        self.pin = pin_no
        self.x = x
        self.y = y
        self.image = pygame.image.load('./simulator/components/speaker/speaker.png')
        self.note = None

    def __str__(self):
        return "Speaker"

    def draw(self, surface):
        rect = (self.x, self.y, self.image.get_rect().width, self.image.get_rect().height)
        surface.blit(self.image, rect)

    def play_tone(self, pin: int, value: str):
        print("speaker:play_tone")

        cmd = QueryString.find(value, 'cmd')
        frequency = QueryString.find(value, 'frequency')
        duration = QueryString.find(value, 'duration')

        print(f"speaker:play_tone. cmd = {cmd}, frequency = {frequency}, duration = {duration}")

        if int(cmd) == 0:
            if self.note is None:
                self.note = Note(int(frequency))

            print("Playing note")
            self.note.play()
        elif int(cmd) == 1:
            if self.note is not None:
                print("Stopping note")
                self.note.stop()