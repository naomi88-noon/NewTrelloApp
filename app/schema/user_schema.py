from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    complete: bool
    
class UserRead(BaseModel):
    id: int
    name: str
    email: str
    complete: bool

    class Config:
        orm_mode = True
    
class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    complete: Optional[bool] = None
    