from pydantic import BaseModel
from typing import List

from .message_base import MessageBase

class ComponentMessage(BaseModel):
    name: str
    pin: int
    x: int
    y: int

class SetupMessage(BaseModel):
    message_type: str
    window_title: str
    components: List[ComponentMessage]

    # def __init__(self):
    #     self.message_type = 'SetupMessage'