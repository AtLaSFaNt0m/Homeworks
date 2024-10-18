from fastapi import FastAPI
from routers import task, user
from backend.db import engine, Base  # Импортируем engine и Base
from models import User, Task  # Импортируем модели

app = FastAPI()

# Создаем таблицы при запуске приложения
Base.metadata.create_all(bind=engine)

app.include_router(task.router)
app.include_router(user.router)

@app.get('/')
async def root():
    return {"message": "Welcome to Taskmanager"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
