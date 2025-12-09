from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 
import os 
from sqlmodel import Session


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:noon8899@localhost:3306/trello_app"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    """Dependency to get SQLModel DB session."""
    with Session(engine) as session:
        yield session