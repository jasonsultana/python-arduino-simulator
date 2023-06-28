from ...components.component_factory import ComponentFactory
from ...components.led.led import Led
from ...breadboard.breadboard import Breadboard
from ...core.window import Window
from ..setup_message import SetupMessage
from ..message_base import MessageBase

class SetupMessageHandler:
    def handles(self, message: MessageBase) -> bool:
        return isinstance(message, SetupMessage)
    
    def handle(self, message: SetupMessage, window: Window, breadboard: Breadboard):
        window.title = message.window_title

        # add components to the breadboard
        for component in message.components:
            breadboard.add(ComponentFactory.create_component(component))