from sqlalchemy.orm import Session
from app.schema.user_schema import UserCreate, UserUpdate
from app.model import User

class UserRepo:
    def __init__(self):
        self.model = User
    def create_user(self, db: Session, user: UserCreate):
        new_user = user
            
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    
    
    def get_all_users(self, db:Session):
        return db.query(self.model).all()
    
    
    def get_user_by_id(self, db:Session, user_id: int):
        return db.query(self.model).filter(self.model.id == user_id).first()
    
    def update_user(self, db:Session, user_id: int, updated_data: UserUpdate):
        user = self.get_user_by_id(db, user_id)
        if not user:
            return None
        
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(user, key, value)

        
        
        db.commit()
        db.refresh()
        return
    
    
    def delete_user(self, db: Session, user_id: int):
        user = self.get_user_by_id(db, user_id)
        if not user:
            return None

        db.delete(user)
        db.commit()

        return True