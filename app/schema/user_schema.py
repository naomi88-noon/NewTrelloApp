from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional



class Login(BaseModel):
    name: str
    password: str

class UserCreate(BaseModel):
    username: str = Field(..., min_length=1)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    password: str = Field(..., min_length=6)
    
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    email: Optional[str] = Field(None, pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    password: Optional[str] = Field(None, min_length=6)
    
    model_config = ConfigDict(from_attributes=True)


class UserRead(BaseModel):
    id: int
    name: Optional[str] = None
    email: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
