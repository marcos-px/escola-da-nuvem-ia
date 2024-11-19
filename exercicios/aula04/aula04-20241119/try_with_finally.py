"""
try:
O mundo ideal
except:
Se der algum problema
finally:
De todo jeito vai rodar.

enumerate
"""

try: 
    arquivo = open("dados.txt", "r")
    print(arquivo.read)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
finally:
    print("Encerrando operação.")
    if 'arquivo' in locals():
        arquivo.close()