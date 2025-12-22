from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.board_schema import CreateBoard, BoardRead, UpdateBoard
from app.service.service_board import BoardService



router = APIRouter()
board_service = BoardService()

@router.post("", response_model=BoardRead, status_code=status.HTTP_201_CREATED)
def create_board(board_data: CreateBoard, db: Session = Depends(get_db)):
    """Create a new board"""
    try:
       board = board_service.create_board(db,board_data )
       return board
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
@router.get("/{board_id}", response_model=BoardRead)
def get_board(board_id: int, db: Session = Depends(get_db)):
    """Get board by ID"""
    try:
        board = board_service.get_board_by_id(db, board_id)
        return board
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
        
@router.get("", response_model=list[BoardRead])
def get_all_boards(owner_id: int, db: Session = Depends(get_db)):
    """Get all boards"""
    try:
        boards = board_service.get_all_boards(db, owner_id)
        return boards
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        ) 
        
        
@router.put("/{board_id}", response_model=BoardRead)
def update_board(board_id: int, board_data: UpdateBoard, db: Session = Depends(get_db)):
    """Update board"""
    try:
        board = board_service.update_board(db, board_id, board_data)
        return board
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
        
@router.delete("/{board_id}", status_code=status.HTTP_200_OK)
def delete_board(board_id: int, db: Session = Depends(get_db)):
    """Delete board"""
    try:
        board_service.delete_board(db, board_id)
        return {"detail": "Board deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )