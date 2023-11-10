from infra.configs.base import Base
from sqlalchemy import create_engine,Column,Integer,String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class Manager(Base):
    __tablename__ = 'manager'
    id = Column(Integer, primary_key=True)
    id_employe = Column(Integer, ForeignKey('employe.id'))
    unit = Column(String(30), nullable=False)
    employe = relationship("Employe", back_populates="manager")
