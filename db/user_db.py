from typing import Dict
from pydantic import BaseModel

#instanciar
class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

# Base Ficticia
# los ** hacen un mapeo de los aributos de la clase
database_users = Dict[str, UserInDB]
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24","password":"root","balance":12000}),
    "andres18": UserInDB(**{"username":"andres18","password":"hola","balance":34000}),
}

#retornar info cuando "pregunten" por usuario
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db