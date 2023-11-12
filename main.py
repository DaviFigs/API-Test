from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
#Queries
from functions.query_defs.employ_query import EmployeQuery
from functions.query_defs.manager_query import ManageQuery
app = FastAPI()

@app.get('/home')
def home():
    return {'msg':'Welcome to my API '}

@app.post('/register')
def register_new_employe(option:int,name:str, cpf:str,salary:float, action:str):
    try:
        employe = EmployeQuery()
        insert = employe.insert_employe(option, name, cpf, salary, action)
        return {'added':insert}
    except:
        return{'error':'Something happens!'}
    
    
@app.get('/get_all_employes')
def all_employe():
    try:
        employ = EmployeQuery()
        data = employ.select_all()
        print(data)
        return {'data':data}
    except:
        return {'error':'Something happens'}
    
@app.get('/get_all_managers')
def all_managers():
    try:
        managers = ManageQuery()
        data = managers.select_managers()
            
        return {'managers':data}
    except:
        return {'error':'Something Happens'}



