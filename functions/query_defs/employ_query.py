from functions.conn_def import return_session
from functions.query_defs.manager_query import ManageQuery
from functions.query_defs.operator_query import OperatorQuery
from functions.query_defs.supervisor_query import SupervisorQuery
from models.models import Employe

session = return_session()
class EmployeQuery:
    def __init__(self) -> None:
        self.session = return_session()

    def insert_employe(self, option,name, cpf,salary, action):
        employe = Employe(name = name, cpf = cpf, salary = salary)
        session.add(employe)
        session.commit()
        emp_id = employe.id
        if option == 1:
            manager = ManageQuery()
            new_manager = manager.insert_manager(emp_id,action)
            session.add(new_manager)
            
        elif option ==  2:
            operator = OperatorQuery()
            new_operator = operator.insert_operator(emp_id,action)
            session.add(new_operator)
        elif option ==3:
            supervisor = SupervisorQuery()
            new_supervisor = supervisor.insert_supervisor(emp_id, action)
            session.add(new_supervisor)
        session.commit()
        session.close()
        return {'Message':f'A new employe and his function was created'}

    def select_all(self):
        data = session.query(Employe).all()
        session.close()
        return data
        