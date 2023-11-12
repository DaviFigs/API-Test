from functions.conn_def import return_session
from models.models import Manager

class ManageQuery:
    def insert_manager(self, employe_id:int, unit:str):
        manager = Manager(id_employe = employe_id, unit = unit)
        return manager

