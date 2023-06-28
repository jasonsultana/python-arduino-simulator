from ...components.led.led import Led
from ...breadboard.breadboard import Breadboard
from ...core.window import Window
from ..setup_message import SetupMessage
from ..message_base import MessageBase

class SetupMessageHandler:
    def handles(self, message: MessageBase) -> bool:
        return isinstance(message, SetupMessage)
    
    def handle(self, message: MessageBase, window: Window, breadboard: Breadboard):
        window.title = message.window_title

        # add components to the breadboard
        for component in message.components:
            if component.name == 'led':
                breadboard.add(Led(component.pin, component.x, component.y))

            # todo: Perhaps a component factory would be best here