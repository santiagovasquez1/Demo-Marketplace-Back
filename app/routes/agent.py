from fastapi import APIRouter
from clients.db import conn
from models.agents import agent
from controllers.agent_controller import AgentController



agents= APIRouter()
@agents.get("/agents")
def get_agents():
    result = AgentController().get_agents()
    return [dict(row._mapping) for row in result] 