from typing import Optional
from pydantic import BaseModel

class CreateTask(BaseModel):
    title: str
    complete: bool
    description: str
    owner_id: int
    board: int

    
    
class ReadTask(BaseModel):
    id : int
    title : str

    class Config:
        orm_mode = True 
        
        
class UpdateTask(BaseModel):
    id : Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    board:Optional[int] = None
    complete:Optional[bool] = None