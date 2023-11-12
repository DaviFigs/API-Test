from functions.conn_def import return_session
from models.models import Manager ,Employe
from functions.aux_defs import filter_search

class ManageQuery:
    def __init__(self) -> None:
        self.session = return_session()
        
    def insert_manager(self, employe_id:int, unit:str):
        manager = Manager(id_employe = employe_id, unit = unit)
        return manager
    
    def select_managers(self,position):
        managers = self.session.query(Manager)\
            .join(Employe, Employe.id == Manager.id_employe)\
            .with_entities(
                Employe.name, 
                Employe.cpf,
                Employe.salary,
                Manager.unit
            ).all()
        list_managers = filter_search(managers, position)   
        
        self.session.close()
        return list_managers


