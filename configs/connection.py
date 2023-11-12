from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
USER = 'root'
PASSWORD = 'mysql'
HOST = 'localhost'
DB = 'api'
PORT = '3306'

CONN_STRING = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONN_STRING, echo =True)
Session = sessionmaker(bind=engine)
session = Session()