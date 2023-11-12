from functions.conn_def import return_session
from models.models import Supervisor,Employe
from functions.aux_defs import filter_search
class SupervisorQuery:
    def __init__(self) -> None:
        self.session = return_session()

    def insert_supervisor(self, employe_id:int, sector:str):
        supervisor = Supervisor(id_employe = employe_id, sector = sector)
        return supervisor
    
    def select_supervisors(self, position):
        supervisors = self.session.query(Supervisor)\
            .join(Employe, Employe.id == Supervisor.id_employe)\
            .with_entities(
                Employe.name,
                Employe.cpf, 
                Employe.salary,
                Supervisor.sector
            ).all()
        list_operators = filter_search(supervisors, position)
        self.session.close()
        return list_operators
    