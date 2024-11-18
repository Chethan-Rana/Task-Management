from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class TaskStatus(str, Enum):
    NEW = "NEW"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"


class BaseTaskDetail(BaseModel):
    title: str
    description: Optional[str]
    due_date: date
    status: TaskStatus = TaskStatus.NEW

    class Config:
        use_enum_values = True


class TaskDetail(BaseTaskDetail):
    user_id: int


class Task(BaseTaskDetail):
    id: int
    user_id: int

    class Config:
        from_attributes = True
