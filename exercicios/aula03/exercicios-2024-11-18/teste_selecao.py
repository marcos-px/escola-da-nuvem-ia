"""
Leia 4 números inteiros
B > C
D > A

C + D > A+ B

C e D > 0

A % 2 == 0

"Valores Aceitos"

"Valores nao Aceitos
"""

A, B, C, D = map(int, input().split())

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores Aceitos")
else: 
    print("Valores não aceitos")

#Chegar em um valor sequencial que atinja o pedido no exercício

#Criar validação para que não seja sequencial