from sqlalchemy.orm import Session
from app.schema.task_schema import CreateTask , UpdateTask
from app.model import Task


class TaskRepo:
    def __init__(self):
        self.model = Task
        
    def create_task(self, db: Session, task: CreateTask):
        new_task = Task(
            name=task.name,
            complete=task.complete,
            board_id=task.board_id,
            owner_id=task.owner_id,
            
)
        
        
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    
    def get_all_task(self, db:Session, user_id: int, Board_id: int):
        if Board_id:
            return db.query(self.model).filter(Task.owner_id == user_id, Task.board_id == Board_id).all()
        else:
            return db.query(self.model).filter(Task.owner_id == user_id).all()
    
    
    def get_task_by_id(self, db:Session, Task_id: int):
        return db.query(self.model).filter(self.model.id == Task_id).first()
    

    def task_update(self, db:Session, task: Task, updated_data: UpdateTask):
       
        update_dict = updated_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(task, key, value)
        
        
        db.commit()
        db.refresh(task)
         
        return task
     
     
    def delete_task(self, db: Session, task: Task):

        db.delete(task)
        db.commit()
        return True