from fastapi import APIRouter
from clients.db import conn
from models.tablas_models import Tables


class CitiesController:
    def __init__(self):
        self.Table = Tables()

    def get_cities(self):
       return conn.execute(self.Table.cities().select()).fetchall()
    
