from simulator.messages.command_message import CommandMessage
from ...breadboard.breadboard import Breadboard
from ...core.window import Window
from ..message_base import MessageBase

class CommandMessageHandler:
    def handles(self, message: MessageBase) -> bool:
        return isinstance(message, CommandMessage)
    
    def handle(self, message: CommandMessage, window: Window, breadboard: Breadboard):
        # find the component on the board connected to the corresponding pin
        for component in breadboard.components:
            if component.pin == message.pin:
                if message.command_text == "digital_write":
                    component.digital_write(int(message.command_value))

        # if the command text is digital_write, invoke the digital_write method on the component

        # todo: Add support for potentially more commands
        pass