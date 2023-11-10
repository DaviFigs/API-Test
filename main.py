#Here we gonna make requests for server
from fastapi import FastAPI
from models import Employe,Supervisor,Manager,Operator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import CONN
from defs import register_new_person
app = FastAPI()

def return_session():#This function returns the session function witch we will use to access database
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind = engine)
    return Session()


@app.get('/home')
def home():
    return {'msg':'Welcome to my API '}

@app.post('/register')
def register_new_employe(option:int,name:str, cpf:str,salary:float, work:str):
    try:
        employe = Employe(name = name, cpf = cpf, salary = salary)
        session = return_session()
        if option == 1:#register supervisor
            employe.supervisor = [Supervisor(sector = work)]
        elif option == 2:
            employe.manager = [Manager(unit = work)]
        elif option == 3:
            employe.operator = [Operator(function = work)]
        session.add(employe)
        session.commit()
    
        return {'success':'User was created!'}
    except:
        return {'error':'erro'}
    
@app.get('/get_all_employe')
def all_employe():
    try:
        session = return_session()
        employes = session.query(Employe).all()
        return {'employes': employes}
    except:
        pass
        



