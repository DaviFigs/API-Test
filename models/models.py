from sqlalchemy import Column,Integer,String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from configs.connection import engine
from configs.base import Base

class Employe(Base):
    __tablename__ = 'employe'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    cpf = Column(String(11),nullable=False)
    salary = Column(Float, nullable=False)
    supervisor = relationship("Supervisor", back_populates="employe")
    manager = relationship("Manager", back_populates="employe")
    operator = relationship("Operator", back_populates="employe")

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

class Supervisor(Base):
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key= True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    sector = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="supervisor")

Base.metadata.create_all(engine)