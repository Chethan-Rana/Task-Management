from sqlalchemy.orm import Session
from app.schemas.user import UserData
from app.models.db_model import User as UserModel


def create_user(user: UserData, db: Session):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(user_id: int, db: Session):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_all_users(db: Session):
    return db.query(UserModel).all()


def delete_user(user_id: int, db: Session):
    db.query(UserModel).filter(UserModel.id == user_id).delete()
    db.commit()


def update_user(
    user_data: UserModel,
    user_update_data: UserData,
    db: Session,
):
    for key, value in user_update_data.model_dump(exclude_unset=True).items():
        setattr(user_data, key, value)

    db.commit()
    db.refresh(user_data)
    return user_data
