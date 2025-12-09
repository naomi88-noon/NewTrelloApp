from fastapi import FastAPI
from app.db.database import engine, Base
from app import model

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Trello Clone API", version="1.0.0")

# # INCLUDE ROUTERS

# # ROOT ENDPOINT
# @app.get("")
# def root():
#     return {"message": "Trello Clone API is running!"}
