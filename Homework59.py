from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
async def read_main():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def user_info(username: str, age: Optional[int] = None):
    if age:
        return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
    return {"message": f"Информация о пользователе. Имя: {username}"}
