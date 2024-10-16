from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутов
app.include_router(task.router)
app.include_router(user.router)
