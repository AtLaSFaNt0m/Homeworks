from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)