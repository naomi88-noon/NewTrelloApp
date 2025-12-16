from sqlalchemy.orm import Session
from app.model.board_model import Board
from app.schema.board_schema import CreateBoard, UpdateBoard
from app.repo.board_repo import BoardRepo


class BoardService:
    def __init__(self):
        self.repo = BoardRepo()
    
    
    def create_board(self, db: Session, data: CreateBoard):
        """Create a new board with validation"""
        new_board = self.repo.create_board(db, data)
        return new_board

        
    def get_all_boards(self, db: Session, owner_id: int):
        """Get all boards for a user"""
        return self.repo.get_all_board(db, owner_id)
    
    def get_board_by_id(self, db: Session, board_id: int):
        """Get board by ID"""
        board = self.repo.get_board_by_id(db, board_id)
        if not board:
            raise Exception("Board not found.")
        return board
    
    def update_board(self, db: Session, board_id: int, updated_data: UpdateBoard):
        """Update board"""
        board = self.get_board_by_id(db, board_id)
        
        return self.repo.update_board(db, board=board, updated_data=updated_data)
    
    def delete_board(self, db: Session, board_id: int):
        """Delete board"""
        board = self.get_board_by_id(db, board_id)
        return self.repo.delete_board(db, board=board)
        