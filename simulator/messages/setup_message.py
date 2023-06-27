from pydantic import BaseModel
from typing import List

class ComponentMessage(BaseModel):
    name: str
    pin: int
    x: int
    y: int

class SetupMessage(BaseModel):
    window_title: str
    components: List[ComponentMessage]