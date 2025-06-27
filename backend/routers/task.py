from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import crud
import schema
from database import get_db

router = APIRouter(prefix="/task", tags=["Tasks"])

@router.get("/all", response_model=List[schema.TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db)

@router.post("/", response_model=schema.TaskOut, status_code=status.HTTP_201_CREATED)
def add_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.put("/{task_id}", response_model=schema.TaskOut)
def edit_task(task_id: str, task: schema.TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task(db, task_id, task)
    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", response_model=schema.TaskOut)
def remove_task(task_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted
