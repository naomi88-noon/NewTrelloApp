from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.database import Base
from sqlalchemy.orm import relationship

class Board(Base):
    __tablename__ ="boards"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    owner_id = Column(Integer, ForeignKey("users.id"))


    task = relationship("Task", back_populates= "boards")
    owner = relationship("User", back_populates="boards")