from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships (lazy loading)
    tasks = relationship("Task", back_populates="owner")
    boards = relationship("Board", back_populates="owner")
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"



