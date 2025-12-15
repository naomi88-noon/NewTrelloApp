from sqlalchemy.orm import Session
from app.model.user_model import User
from app.schema.user_schema import UserCreate, UserUpdate


class UserRepo:
    
    def create_user(self, db: Session, user: UserCreate):
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
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
        update_dict = updated_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(user, key, value)
        
        db.commit()
        db.refresh(user)
        return user
    
    def delete_user(self, db: Session, user: User):
        """Delete user"""
        
        db.delete(user)
        db.commit()
        
        return True