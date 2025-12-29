from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt, JWTError
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.api import user
from app.db.database import get_db
from app.model.user_model import User
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel


router = APIRouter(
    # prefix="/auth",
    # tags=["auth"]
)

SECRET_KEY = "your-secret-key" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


bycrpt_context = CryptContext(
    schemes=["bcrypt_sha256"],
    deprecated="auto"
)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


class CreateUserRequest(BaseModel):
    name: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    user_model = User(
        name=create_user_request.name,
        password = bycrpt_context.hash(create_user_request.password)
    )
    db.add(user_model)
    db.commit()
        
    







