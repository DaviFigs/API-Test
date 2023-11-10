from infra.configs.base import Base
from sqlalchemy import create_engine,Column,Integer,String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class Supervisor(Base):
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key= True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    sector = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="supervisor")
