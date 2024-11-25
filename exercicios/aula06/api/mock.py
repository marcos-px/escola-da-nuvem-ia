import json

response = '{"nome": "Marcos", "cidade": "Sete Lagoas", "idade": "30"}'

dados = json.loads(response)

print(dados['idade'])