#Importei as bibliotecas e módulos
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="API de Consulta de CEP", description="API criada junto com os alunos da EDN para consulta de CEP")

@app.get("/")
def home():
    """
    Rota inicial para verificar se a API está ok.
    """
    return {"message": "Bem vindo à API de Consulta de CEP"}

@app.get("/consulta-cep/{cep}")
def consulta_cep(cep: str):
    """
    Consulta as informações do CEP e devolve o endereço.
    -cep: Deve ser no formato '0000000'
    """

    if len(cep) !=8 or not cep.isdigit():
        raise HTTPException(status_code=400, detail="Este CEP está inválido.")
    
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="O servidor está fora do ar")
    
    data = response.json()

    if "erro" in data:
        raise HTTPException(status_code=404, detail="CEP não encontrado")
    
    return data