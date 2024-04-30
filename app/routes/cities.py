from fastapi import APIRouter
from clients.db import conn
from models.cities import cities
from controllers.cities_controller import CitiesController

from fastapi import HTTPException


city= APIRouter()
@city.get("/cities")
def get_cities():
    result= CitiesController().get_cities()
    return [dict(row._mapping) for row in result]



