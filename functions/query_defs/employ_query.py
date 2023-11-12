from functions.conn_def import return_session
from functions.query_defs.manager_query import ManageQuery
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
            session.commit()
            session.close()
            return {'Message':f'A new manager was created at employe id:{emp_id}'}
        elif option ==  2:
            pass
        elif option ==3:
            pass

    def select_all(self):
        data = session.query(Employe).all()
        session.close()
        return data
        