from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import traceback
from fastapi import HTTPException
from app.api import user
from app.model.user_model import User
from app.schema.user_schema import UserCreate, UserUpdate
from app.db.database import get_db
from fastapi import Depends


class UserRepo:
    
   
    def create_user(self, db: Session, user: UserCreate):
        try:
            new_user = User(
              name=user.name,
              email=user.email,
              password=user.password
        )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except SQLAlchemyError:
          db.rollback()
          traceback.print_exc()
          raise HTTPException(status_code=500, detail= "fail to create user")
     
    def get_all_users(self, db: Session):
        """Get all users"""
        return db.query(User).all()
    
    def get_user_by_id(self, db: Session, user_id: int):
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, db: Session, email: str):
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    def update_user(self, db: Session, user: User, updated_data: UserUpdate):
        """Update user"""
        try:
           update_dict = updated_data.model_dump(exclude_unset=True)
           for key, value in update_dict.items():
            setattr(user, key, value)
        
           db.commit()
           db.refresh(user)
           return user
    
        except SQLAlchemyError:
          db.rollback()
          traceback.print_exc()
          raise HTTPException(status_code=500, detail="fail to update user")
    
    def delete_user(self, db: Session, user: User):
        """Delete user"""
        
        db.delete(user)
        db.commit()
        
        return {"detail": "Task deleted"}