from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from app.db.database import Base
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    complete = Column(Boolean, default=False)


    owner_id = Column(Integer, ForeignKey("users.id"))  
    board_id = Column(Integer, ForeignKey("boards.id"))  
     
    owner = relationship("User", back_populates="tasks",  foreign_keys=[owner_id]) 
    board = relationship("Board", back_populates="tasks", foreign_keys=[board_id]) 
    
    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', owner_id={self.owner_id})>"