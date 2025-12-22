from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import traceback
from fastapi import HTTPException
from app.schema.board_schema import CreateBoard , UpdateBoard
from app.model import Board

class BoardRepo:
    def __init__(self):
        self.model = Board
    def create_board(self, db: Session, board: CreateBoard):
        try:
            new_Board = Board(
                name=board.name,
                description=board.description,
            )
                
            db.add(new_Board)
            db.commit()
            db.refresh(new_Board)
            return new_Board
        except SQLAlchemyError:
            db.rollback()
            traceback.print_exc()
            raise HTTPException(status_code=500, detail= "fail to create board")


    
    def get_all_board(self, db:Session, user_id: int):
     return db.query(self.model).filter(self.model.owner_id == user_id).all()
    
    def get_board_by_id(self, db:Session, board_id: int):
        return db.query(self.model).filter(self.model.id == board_id).first()
    
    
    def update_board(self, db:Session, board: Board, updated_data: UpdateBoard):
        update_dict = updated_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(board, key, value)

        
        try:
            db.commit()
            db.refresh(board)
            return board

        except SQLAlchemyError:
            db.rollback()
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="fail to update board") 
        
        
    def delete_board(self, db: Session, board: Board):

        db.delete(board)
        db.commit()

        return True