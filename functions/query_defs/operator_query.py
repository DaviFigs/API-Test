from functions.conn_def import return_session
from models.models import Operator

class OperatorQuery:
    def __init__(self) -> None:
        self.session = return_session()

    def insert_operator(self, employe_id:int, function:str):
        operator = Operator(id_employe = employe_id, function = function)
        return operator