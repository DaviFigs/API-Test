from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
#Queries
from functions.query_defs.employ_query import EmployeQuery
app = FastAPI()

@app.get('/home')
def home():
    return {'msg':'Welcome to my API '}

@app.post('/register')
def register_new_employe(option:int,name:str, cpf:str,salary:float, action:str):
    employe = EmployeQuery()
    insert = employe.insert_employe(option, name, cpf, salary, action)
    return {'added':insert}

    
    
@app.get('/get_all_employes')
def all_employe():
    employ = EmployeQuery()
    data = employ.select_all()
    return {'data':data}

    
        



