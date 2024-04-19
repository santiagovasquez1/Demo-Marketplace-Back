from fastapi import APIRouter
from clients.db import conn
from models.agents import agent



agents= APIRouter()
@agents.get("/agents")
def get_users():
    result = conn.execute(agent.select()).fetchall()
    return [dict(row._mapping) for row in result] 