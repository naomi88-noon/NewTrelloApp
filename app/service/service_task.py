from sqlalchemy.orm import Session
from app.schema.task_schema import CreateTask, UpdateTask
from app.model.task_model import Task
from app.repo.task_repo import TaskRepo


class TaskService:
    def __init__(self):
        self.repo = TaskRepo()
    
    def create_task(self, db: Session, data: CreateTask):
        """Create a new task with validation"""
        # Create new task
        new_task = self.repo.create_task(db, data)
        return new_task
    
    def get_all_task(self, db: Session, user_id: int, Board_id: int):
        """Get all tasks"""
        return self.repo.get_all_task(db, user_id, Board_id)
    
    def get_task_by_id(self, db: Session, task_id: int):
        """Get task by ID"""
        task = self.repo.get_task_by_id(db, task_id)
        if not task:
            raise Exception("Task not found.")
        return task
    
    def update_task(self, db: Session, task_id: int, updated_data: UpdateTask):
        """Update task"""
        task = self.repo.get_task_by_id(db, task_id)
        return self.repo.task_update(db, task=task, updated_data=updated_data)

        
    def delete_task(self, db: Session, task_id: int):
        """Delete task"""
        task = self.repo.get_task_by_id(db, task_id)
        return self.repo.delete_task(db, task=task)
        
       