from simulator.messages.command_message import CommandMessage
from ...breadboard.breadboard import Breadboard
from ...core.window import Window
from ..message_base import MessageBase

class CommandMessageHandler:
    def handles(self, message: MessageBase) -> bool:
        return isinstance(message, CommandMessage)
    
    def handle(self, message: CommandMessage, window: Window, breadboard: Breadboard):
        component = self.__find_component(breadboard, message.pin)
        if component is None:
                print(f"Warning: Could not find component on pin {message.pin}")
                return
        
        if message.command_text == "digital_write":
            component.digital_write(message.pin, message.command_value)

        if message.command_text == "play_tone":
             component.play_tone(message.pin, message.command_value)
             
        # todo: Add support for potentially more commands

    def __find_component(self, breadboard: Breadboard, pin: int):
        # find the component on the board connected to the corresponding pin
        for component in breadboard.components:
            if component.pin == pin:
                 return component
            
        return None
            