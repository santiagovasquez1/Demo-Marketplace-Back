from sqlalchemy import Table
from clients.db import meta, engine


cities = Table('cities', meta, autoload_with=engine)