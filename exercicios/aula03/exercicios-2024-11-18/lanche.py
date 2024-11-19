"""
1: 4.00,
2: 4.50,
3: 5.00,
4: 2.00,
5: 1.50

"""

codigo, quantidade = map(int,
                          input("Digite o código do produto e a quantidade (separados por espaço): ").split())

precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

total = precos[codigo] * quantidade

print(f"Total: R$ {total:.2f}")

#Continuem colocando casos de erro, se o usuário inserir códigos inexistes ou valores inexistentes