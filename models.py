#Here we are gonug to build our database tables and columns
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'root'
PASSWORD = 'mysql'
HOST = 'localhost'
DB = 'api'
PORT = '3306'

CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONN, echo =True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Person(Base):
    __tablename__ ='Person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    cpf = Column(String(11))

