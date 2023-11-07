#Here we gonna make requests for server
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import CONN

app = FastAPI()

def return_session():#This function returns the session function witch we will use to access database
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind = engine)
    return Session()


@app.get('/home')
def home():
    return {'msg':'Welcome to my API '}

