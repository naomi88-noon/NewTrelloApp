from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.database import Base
from sqlalchemy.orm import relationship

class Board(Base):
    __tablename__ ="boards"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(1024), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))


    owner = relationship("User", back_populates="boards")
    tasks = relationship("Task", back_populates="board", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Board(id={self.id}, name='{self.name}', owner_id={self.owner_id})>"