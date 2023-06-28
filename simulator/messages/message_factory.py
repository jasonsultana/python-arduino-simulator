import json

from .command_message import CommandMessage
from .setup_message import SetupMessage
from .message_base import MessageBase

class MessageFactory:
    @staticmethod
    def createMessage(msg: str):
        message_json = json.loads(msg)
        message = MessageBase(**message_json)
        
        match message.message_type:
            case "setup":
                return SetupMessage(**message_json)
            
            case "command":
                return CommandMessage(**message_json)
            
            case _:
                raise f"Message type {message.message_type} not supported"