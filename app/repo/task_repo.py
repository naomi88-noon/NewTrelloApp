from sqlalchemy.orm import Session
from app.schema.task_schema import CreateTask , UpdateTask
from app.model import Task


class TaskRepo:
    def __init__(self):
        self.model = Task
        
    def create_task(self, db: Session, task: CreateTask):
        new_task = Task(
            title=task.title,
            description=task.description,   
            board=task.board,
            owner_id=task.owner_id,
            
)
        
        
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    
    def get_all_task(self, db:Session):
        return db.query(self.model).all()
    
    
    def get_task_by_id(self, db:Session, Task_id: int):
        return db.query(self.model).filter(self.model.id == Task_id).first()
    

    def task_update(self, db:Session, task: Task, updated_data: UpdateTask):
       
        update_dict = updated_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(task, key, value)
        
        
        db.commit()
        db.refresh(task)
         
        return task
     
     
    def delete_task(self, db: Session, Task_id: int):

        db.delete(Task)
        db.commit()
        return True