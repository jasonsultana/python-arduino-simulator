from pydantic import BaseModel
from .message_base import MessageBase

class CommandMessage(BaseModel):
    message_type: str
    pin: int
    command_text: str
    command_value: str

    # def __init__(self):
    #     self.message_type = 'CommandMessage'
        
    @staticmethod
    def create(pin, command_text, command_value):
        message = CommandMessage()
        message.pin = pin
        message.command_text = command_text
        message.command_value = command_value

        return message