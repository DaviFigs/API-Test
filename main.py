from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
app = FastAPI()

@app.get('/home')
def home():
    return {'msg':'Welcome to my API '}

@app.post('/register')
def register_new_employe(option:int,name:str, cpf:str,salary:float, work:str):
    pass
    
@app.get('/get_all_employes')
def all_employe():
    pass
        



