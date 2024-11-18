from fastapi import FastAPI
import uvicorn

from app.api import user, tasks
from app.database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, tags=["Users"])
app.include_router(tasks.router, tags=["Tasks"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
