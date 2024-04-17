from sqlalchemy import Table
from clients.db import meta, engine


users = Table('users', meta, autoload_with=engine)
