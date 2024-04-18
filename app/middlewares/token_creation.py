from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes usar os.getenv para obtener las variables de entorno

def expire_time(days: int):
    date= datetime.now()
    new_date= date + timedelta(days)
    return new_date


def create_token(data:dict):
    token= jwt.encode({**data, "exp": expire_time(2)}, os.getenv('SECRET_KEY'), algorithm='HS256')
    return token