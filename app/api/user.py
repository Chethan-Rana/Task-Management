from fastapi import APIRouter, Depends, HTTPException

from app.core.user import create_user, update_user, get_all_users, get_user, delete_user
from app.database.database import get_db
from app.schemas.user import User, UserData

router = APIRouter(prefix="/users")


@router.post("/", response_model=User)
def create_new_user(user: UserData, db=Depends(get_db)):
    return create_user(user, db)


@router.get("/{user_id}", response_model=User)
def get_user_data(user_id: int, db=Depends(get_db)):
    user_data = get_user(user_id, db)
    if not (user_data):
        raise HTTPException(status_code=404, detail="User Not Found")
    return user_data


@router.get("/")
def get_users(db=Depends(get_db)):
    return get_all_users(db)


@router.delete("/{user_id}")
def delete_user_data(user_id: int, db=Depends(get_db)):
    user_data = get_user(user_id, db)
    if not (user_data):
        raise HTTPException(status_code=404, detail="The specified user is not found")

    return delete_user(user_id, db)


@router.patch("/{user_id}")
def update_user_data(user_id: int, user_update_data: UserData, db=Depends(get_db)):
    user_data = get_user(user_id, db)
    if not (user_data):
        raise HTTPException(status_code=404, detail="User Not Found")

    return update_user(user_data, user_update_data, db)
