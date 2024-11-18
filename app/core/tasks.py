from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.db_model import Task
from app.schemas.tasks import TaskDetail


def create_task(task_request: TaskDetail, db: Session):
    db_task = Task(**task_request.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(task_id: int, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks(db: Session):
    return db.query(Task).all()


def delete_task(task_id: int, db: Session):
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()


def update_task(task: Task, task_detail: TaskDetail, db: Session):
    for key, value in task_detail.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


def get_tasks_status(db: Session):
    tasks = (
        db.query(Task.status, func.count(Task.id).label("task count"))
        .group_by(Task.status)
        .all()
    )

    tasks_status = [{"status": row[0], "task_count": row[1]} for row in tasks]

    return tasks_status
