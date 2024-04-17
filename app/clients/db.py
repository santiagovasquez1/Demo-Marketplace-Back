from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes usar os.getenv para obtener las variables de entorno
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')


# Crea la cadena de conexión
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# Crea el motor de SQLAlchemy
engine = create_engine(connection_string)
conn = engine.connect()
meta = MetaData()


