from infra.configs.base import Base
from sqlalchemy import create_engine,Column,Integer,String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


class Employe(Base):
    __tablename__ = 'employe'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    cpf = Column(String(11),nullable=False)
    salary = Column(Float, nullable=False)
    supervisor = relationship("Supervisor", back_populates="employe")
    manager = relationship("Manager", back_populates="employe")
    operator = relationship("Operator", back_populates="employe")
