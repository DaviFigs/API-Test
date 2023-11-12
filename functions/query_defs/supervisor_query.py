from functions.conn_def import return_session
from models.models import Supervisor
class SupervisorQuery:
    def __init__(self) -> None:
        self.session = return_session()

    def insert_supervisor(self, employe_id:int, sector:str):
        supervisor = Supervisor(id_employe = employe_id, sector = sector)
        return supervisor
    