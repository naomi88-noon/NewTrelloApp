from typing import Optional
from pydantic import BaseModel

class CreateTask(BaseModel):
    name: str
    complete: bool 
    owner_id: int
    board_id: int

    
    
class ReadTask(BaseModel):
    id : int
    name : str
    owner_id: int
    board_id: int
    complete: bool


    class Config:
        orm_mode = True 
        
        
class UpdateTask(BaseModel):
    name: Optional[str] = None
    board_id:Optional[int] = None
    complete:Optional[bool] = None
    