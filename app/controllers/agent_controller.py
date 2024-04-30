from fastapi import APIRouter
from clients.db import conn
from models.tablas_models import Tables


class AgentController:
    def __init__(self):
        self.Table = Tables()

    def get_agents(self):
       return conn.execute(self.Table.agent().select()).fetchall()
    
