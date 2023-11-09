#Here we are gonug to build our database tables and columns
from sqlalchemy import create_engine,Column,Integer,String, Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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

class Employe(Base):
    __tablename__ = 'employe'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    cpf = Column(String(11),nullable=False)
    salary = Column(Float, nullable=False)
    supervisor = relationship("Supervisor", back_populates="employe")
    manager = relationship("Manager", back_populates="employe")
    operator = relationship("Operator", back_populates="employe")

class Supervisor(Base):
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key= True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    sector = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="supervisor")

class Manager(Base):
    __tablename__ = 'manager'
    id = Column(Integer, primary_key=True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    unit = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="manager")


class Operator(Base):
    __tablename__ = 'operator'
    id = Column(Integer, primary_key=True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    function = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="operator")


Base.metadata.create_all(engine)










    


