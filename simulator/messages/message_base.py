from pydantic import BaseModel

class MessageBase(BaseModel):
    message_type: str