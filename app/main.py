from fastapi import FastAPI
from routers import task
from routers import user
from app.models.user import User
from app.models.task import Task
app= FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))

print(CreateTable(Task.__table__))