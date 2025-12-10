from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
class UserRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
    
class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None
    