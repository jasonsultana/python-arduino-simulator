from pydantic import BaseModel

class CommandMessage(BaseModel):
    pin: int
    command_text: str