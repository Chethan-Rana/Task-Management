from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:1234@localhost:5432/task_db"
)

DB_NAME = "task_db"


def create_database_if_not_found():
    connection = psycopg2.connect(DATABASE_URL)
    connection.autocommit = True
    cursor = connection.cursor()

    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Data base { DB_NAME } created successfully")

    else:
        print(f"Data base {DB_NAME} already exists")

    cursor.close()
    connection.close()


# Used for Database creation
# create_database_if_not_found()

engine = create_engine(DATABASE_URL)
Session = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
