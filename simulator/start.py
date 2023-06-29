# External
import time
import zmq
import pygame
from threading import *

# Internal
from .core.header import Header
from .messages.setup_message import SetupMessage
from .breadboard.breadboard import Breadboard
from .components.component import Component
from .components.led.led import Led
from .core.window import Window
from .messages.message_factory import MessageFactory
from .messages.handlers.setup_message_handler import SetupMessageHandler
from .messages.handlers.command_message_handler import CommandMessageHandler

pygame.init()
screen = pygame.display.set_mode((1000, 750))

lock = Lock()
window = Window()
breadboard = Breadboard(screen, top=50)
header = Header(screen)
message_handlers = [
    SetupMessageHandler(),
    CommandMessageHandler()
]

def receive_messages():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    #  Wait for next request from client
    while True:
        message = socket.recv().decode('utf-8')
        print("Received request: %s" % message)

        message_obj = MessageFactory.createMessage(message)

        with lock:
            print("message thread acquired lock.")
            for handler in message_handlers:
                if handler.handles(message_obj):
                    handler.handle(message_obj, window, breadboard)
                    
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
            #print("ui thread acquired lock.")
            pygame.display.set_caption(window.title)

        # Show the new frame
        pygame.display.flip()

        time.sleep(0.1)

    # deactivates the pygame library
    pygame.quit()

# main thread is for update_ui
# background thread is for receive_messages

Thread(target=receive_messages, daemon=True).start()
update_ui()