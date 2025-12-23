from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.user_schema import UserCreate, UserRead, UserUpdate, Login
from app.service.service_user import UserService
from app.auth import get_current_user
from app.model.user_model import User
from app.auth import  create_access_token

router = APIRouter()
user_service = UserService()


@router.post("/")
def login(data:Login, db: Session = Depends(get_db)):
    """User login"""
    return user_service.login(data, db)


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    try:
        user = user_service.create_user(db, user_data)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    try:
        user = user_service.get_user_by_id(db, user_id)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@router.get("", response_model=list[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    """Get all users"""
    try:
        users = user_service.get_all_users(db)
        return users
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    """Update user"""
    try:
        user = user_service.update_user(db, user_id=user_id, updated_data=user_data)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete user"""
    try:
        user_service.delete_user(db, user_id)
        return {"detail": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )