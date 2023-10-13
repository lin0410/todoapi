from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    hashed_password: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    task: str
    completed: bool = False
    dateOfRealisation: str # iso 8601(%Y-%m-%d)
    


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):

    completed: bool


class TaskDelete(BaseModel):

    completed: bool


class TaskDateUpdate(BaseModel):

    dateOfRealisation: str
