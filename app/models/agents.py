from sqlalchemy import Table
from clients.db import meta, engine


agent = Table('agent', meta, autoload_with=engine)