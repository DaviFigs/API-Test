from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from configs.connection import CONN_STRING


def return_session():
    engine = create_engine(CONN_STRING, echo=True)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session