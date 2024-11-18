from pydantic import BaseModel
from typing import List
from app.schemas.tasks import Task


class UserData(BaseModel):
    name: str
    email: str


class User(UserData):
    id: int
    tasks: List[Task] = []

    class config:
        from_attributes = True
