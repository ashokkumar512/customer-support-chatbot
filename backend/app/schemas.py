from pydantic import BaseModel
from typing import List

class MessageCreate(BaseModel):
    role: str
    content: str

class Message(BaseModel):
    id: int
    role: str
    content: str

    class Config:
        orm_mode = True

class Session(BaseModel):
    id: int
    messages: List[Message] = []

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    sessions: List[Session] = []

    class Config:
        orm_mode = True
