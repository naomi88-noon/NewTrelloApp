from typing import Optional
from pydantic import BaseModel


class CreateBoard(BaseModel):
    name:str
    description: str
    

class BoardRead(BaseModel):
    id : int
    name : str
    description: str
   
   
    class Config:
        orm_mode = True 
 
class UpdateBoard(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None  
    
     