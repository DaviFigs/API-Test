from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
#Queries
from functions.query_defs.employ_query import EmployeQuery
from functions.query_defs.manager_query import ManageQuery
from functions.query_defs.operator_query import OperatorQuery
from functions.query_defs.supervisor_query import SupervisorQuery
app = FastAPI()


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
    
@app.post('/select_employs_by_opsition')
def employes_by_work(position:int):
    try:
        print("1-Manager")
        if position == 1:
            manager = ManageQuery()
            data = manager.select_managers(position)
        elif position == 2:
            operator = OperatorQuery()
            data = operator.select_operators(position)
        elif position == 3:
            supervisor = SupervisorQuery()
            data = supervisor.select_supervisors(position)

        print(data)
        return {'managers':data}
    except:
        return {'error':'Something Happens'}
@app.post('/comission')
def add_comission(position:int, num_sold):
    pass
    


