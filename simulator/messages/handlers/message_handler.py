from simulator.breadboard.breadboard import Breadboard
from ...core.window import Window
from ..message_base import MessageBase

class MessageHandler:
    def handles(self, message: MessageBase) -> bool:
        return False
    
    def handle(self, message: MessageBase, window: Window, breadboard: Breadboard):
        pass