from fastapi import APIRouter
from clients.db import conn
from models.regions import regions

from fastapi import HTTPException


region= APIRouter()
@region.get("/regions")
def get_users():
    result = conn.execute(regions.select()).fetchall()
    return [dict(row._mapping) for row in result]
