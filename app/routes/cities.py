from fastapi import APIRouter
from clients.db import conn
from models.cities import cities

from fastapi import HTTPException


city= APIRouter()
@city.get("/cities")
def get_users():
    result = conn.execute(cities.select()).fetchall()
    return [dict(row._mapping) for row in result]
