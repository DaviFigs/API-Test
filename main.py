from fastapi import FastAPI
from sqlalchemy import create_engine,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = FastAPI()
def return_session():    

    USER = 'root'
    PASSWORD = ''
    HOST = 'localhost'
    DB = 'api'
    PORT = '3306'

    CONN = f'mysql+pymysql;//{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

    engine = create_engine(CONN, echo =True)
    Session = sessionmaker(bind=engine)
    return Session

