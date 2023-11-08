from models import Employe
def register_new_person(name,cpf,salary) -> Employe: 
    employe = Employe(name = name, cpf = cpf, salary = salary)
    return employe
