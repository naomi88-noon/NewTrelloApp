from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.model.user_model import User
from app.schema.user_schema import UserCreate, UserUpdate
from app.repo.user_repo import UserRepo


class UserService:
    
    def __init__(self):
        self.repo = UserRepo()
          
    
 
    def create_user(self, db: Session, data: UserCreate):
        """Create a new user with validation"""
        # Check if user already exists
        existing_user = self.repo.get_user_by_email(db, data.email)
        if existing_user:
            raise Exception("Account already exists.")
        
        # Create new user
        new_user = self.repo.create_user(db, data)
        return new_user
    
    def get_all_users(self, db: Session):
        """Get all users"""
        return self.repo.get_all_users(db)
    
    def get_user_by_id(self, db: Session, user_id: int):
        """Get user by ID"""
        user = self.repo.get_user_by_id(db, user_id)
        if not user:
            raise Exception("User not found.")
        return user
    
    def update_user(self, db: Session, user_id: int, updated_data: UserUpdate):
        """Update user"""
        user = self.get_user_by_id(db, user_id)
        
        return self.repo.update_user(db, user=user, updated_data=updated_data)
        
        
        
    def delete_user(self, db: Session, user_id: int):
        """Delete user"""
        user = self.get_user_by_id(db, user_id)
    
        return self.repo.delete_user(db, user=user)
       
