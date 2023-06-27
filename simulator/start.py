# External
import time

import zmq
import pygame
import json
from threading import *

# Internal
from .core.header import Header
from .messages.setup_message import SetupMessage
from .breadboard.breadboard import Breadboard
from .components.component import Component
from .components.led.led import Led

pygame.init()
screen = pygame.display.set_mode((1000, 750))

lock = Lock()
window_caption = ''
breadboard = Breadboard(screen, top=50)
header = Header(screen)

def receive_messages():
    global window_caption
    
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    #  Wait for next request from client
    while True:
        message = socket.recv().decode('utf-8')
        print("Received request: %s" % message)

        message_json = json.loads(message)
        # TODO: Handle different types of messages
        # SetupMessage
        # CommandMessage

        message_obj = SetupMessage(**message_json)

        with lock:
            print("message thread acquired lock.")
            window_caption = message_obj.window_title

            # add components to the breadboard
            for component in message_obj.components:
                if component.name == 'led':
                    breadboard.add(Led(component.pin, component.x, component.y))
                # todo: Perhaps a component factory would be best here

        #  Send reply back to client
        socket.send(b"OK")

        # sleep for 100ms
        time.sleep(0.1)

def update_ui():
    status = True
    while status:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False

        # Background Color
        screen.fill((0, 0, 0))

        # Update header
        mouse_pos = pygame.mouse.get_pos()
        header.set_mouse_pos(mouse_pos[0], mouse_pos[1])
        header.set_title(header.lbl_title.default_text)
        header.draw()

        # Breadboard
        breadboard.draw()

        with lock:
            print("ui thread acquired lock.")
            pygame.display.set_caption(window_caption)

        # Show the new frame
        pygame.display.flip()

        time.sleep(1)

    # deactivates the pygame library
    pygame.quit()

# main thread is for update_ui
# background thread is for receive_messages

Thread(target=receive_messages, daemon=True).start()
update_ui()