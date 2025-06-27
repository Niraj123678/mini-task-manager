import uuid
from sqlalchemy.orm import Session
from models import Task
from schema import TaskCreate, TaskUpdate

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_id: str):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    new_task = Task(
        id=str(uuid.uuid4()),
        title=task.title,
        description=task.description,
        status=task.status
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def update_task(db: Session, task_id: str, task_data: TaskUpdate):
    task = get_task(db, task_id)
    if task is None:
        return None
    task.title = task_data.title
    task.description = task_data.description
    task.status = task_data.status
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: str):
    task = get_task(db, task_id)
    if task is None:
        return None
    db.delete(task)
    db.commit()
    return task
