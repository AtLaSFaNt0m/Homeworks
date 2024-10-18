from backend.db import Base, engine
from models import User, Task

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)
