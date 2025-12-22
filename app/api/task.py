from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import get_db 
from app.schema.task_schema import CreateTask, ReadTask, UpdateTask
from sqlalchemy.orm import Session
from app.service.service_task import TaskService




router = APIRouter()
task_service = TaskService()


@router.post("", response_model=ReadTask, status_code=status.HTTP_201_CREATED)
def create_task(task_data: CreateTask, db: Session = Depends(get_db)):
    """Create a new task"""
    try:
        task = task_service.create_task(db, task_data)
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
@router.get("/{task_id}", response_model=ReadTask)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Get task by ID"""
    try:
        task = task_service.get_task_by_id(db, task_id)
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
        
@router.get("", response_model=list[ReadTask])
def get_all_tasks(board_id: int, user_id: int, db: Session = Depends(get_db)):
    """Get all tasks"""
    try:
        tasks = task_service.get_all_task(db, user_id, board_id)
        return tasks
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )    
        
@router.put("/{task_id}", response_model=ReadTask)
def update_task(task_id: int, task_data: UpdateTask, db: Session = Depends(get_db)):
    """Update task"""
    try:
        task = task_service.update_task(db, task_id, task_data)
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
@router.delete("/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete task"""
    try:
       return task_service.delete_task(db, task_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )