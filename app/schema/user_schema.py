from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
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
    name: str
    email: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)
