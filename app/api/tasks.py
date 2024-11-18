from fastapi import APIRouter, Depends, HTTPException

from app.core.tasks import (
    create_task,
    get_task,
    get_tasks,
    get_tasks_status,
    update_task,
    delete_task,
)
from app.database.database import get_db
from app.schemas.tasks import TaskDetail, Task

router = APIRouter(prefix="/tasks")


@router.get(path="/task_status")
def get_status(db=Depends(get_db)):
    print("Get status update is called :")
    return get_tasks_status(db)


@router.post("/", response_model=Task)
def create_new_task(user: TaskDetail, db=Depends(get_db)):
    return create_task(user, db)


@router.get("/{task_id}", response_model=Task)
def get_task_data(task_id: int, db=Depends(get_db)):
    task_data = get_task(task_id, db)
    if not (task_data):
        raise HTTPException(status_code=404, detail="Task Not Found")
    return task_data


@router.get("/")
def get_all_tasks(db=Depends(get_db)):
    return get_tasks(db)


@router.delete("/{task_id}")
def delete_task_data(task_id: int, db=Depends(get_db)):
    task_data = get_task(task_id, db)
    if not (task_data):
        raise HTTPException(status_code=404, detail="The specified task is not found")

    return delete_task(task_id, db)


@router.patch("/{task_id}")
def update_task_data(task_id: int, user_update_data: TaskDetail, db=Depends(get_db)):
    task_data = get_task(task_id, db)
    if not (task_data):
        raise HTTPException(status_code=404, detail="Task Not Found")

    return update_task(task_data, user_update_data, db)
