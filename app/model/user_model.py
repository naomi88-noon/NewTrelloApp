from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base
from sqlalchemy.orm import relationship
from app.model.task_model import Task
from app.model.board_model import Board


class User(Base):
     __tablename__ = "users"
     
     id = Column(Integer, primary_key=True, index=True )
     name = Column(String(255))
     email = Column(String(255))
     password = Column(String(255))
     

     task= relationship(Task, back_populates= "owner")
     board = relationship(Board, back_populates= "owner")
    


    