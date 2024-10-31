from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task
from schemas import CreateTask, UpdateTask
from sqlalchemy import select
from slugify import slugify

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    raise HTTPException(status_code=404, detail="Task was not found")

@router.post("/create")
async def create_task(task: CreateTask, db: Annotated[Session, Depends(get_db)]):
    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=task.user_id,
        slug=slugify(task.title)
    )
    db.add(new_task)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update/{task_id}")
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    db_task = db.scalar(select(Task).where(Task.id == task_id))
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    
    db_task.title = task.title
    db_task.content = task.content
    db_task.priority = task.priority
    db_task.slug = slugify(task.title)
    db.commit()
    
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    db_task = db.scalar(select(Task).where(Task.id == task_id))
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    
    db.delete(db_task)
    db.commit()
    
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}