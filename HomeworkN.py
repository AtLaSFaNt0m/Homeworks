from fastapi import FastAPI, Path
from typing import Annotated, Optional

app = FastAPI()

@app.get("/")
async def read_main():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/{username}")
async def user_info_no_age(username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20)]):
    return {"message": f"Информация о пользователе. Имя: {username}"}
