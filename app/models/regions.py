from sqlalchemy import Table
from clients.db import meta, engine


regions = Table('regions', meta, autoload_with=engine)