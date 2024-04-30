from sqlalchemy import Table
from clients.db import meta, engine

class Tables():

    @staticmethod
    def users():
        return Table('users', meta, autoload_with=engine)
    
    @staticmethod
    def agent():
        return Table('agent', meta, autoload_with=engine)
    
    @staticmethod
    def cities():
        return Table('cities', meta, autoload_with=engine)
    
    @staticmethod
    def regions():
        return Table('regions', meta, autoload_with=engine)