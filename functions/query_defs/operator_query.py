from functions.conn_def import return_session
from models.models import Operator,Employe
from functions.aux_defs import filter_search

class OperatorQuery:
    def __init__(self) -> None:
        self.session = return_session()

    def insert_operator(self, employe_id:int, function:str):
        operator = Operator(id_employe = employe_id, function = function)
        return operator

    def select_operators(self,position):
        operators = self.session.query(Operator)\
            .join(Employe, Employe.id == Operator.id_employe)\
            .with_entities(
                Employe.name,
                Employe.cpf,
                Employe.salary,
                Operator.function
            ).all()
        list_operators = filter_search(operators, position)
        self.session.close()
        return list_operators