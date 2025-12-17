from fastapi import FastAPI
from app.db.database import engine, Base

# Import all models to register them with Base
from app.model.user_model import User
from app.model.task_model import Task
from app.model.board_model import Board

from app.api.user import router as user_router
from app.api.board import router as board_router
from app.api.task import router as task_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Trello Clone API",
    version="1.0.0",
    description="A Trello clone built with FastAPI"
)

# ROOT ENDPOINT
@app.get("/")
def root():
    return {"message": "Trello Clone API is running!"}


# INCLUDE ROUTERS
app.include_router(user_router, prefix="/api/user", tags=["User"])
app.include_router(board_router, prefix="/api/board", tags=["Board"])
app.include_router(task_router, prefix="/api/task", tags=["Task"])
