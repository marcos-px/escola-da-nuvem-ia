#if elif else

"""
0 -400 - 15%
400.01 - 800.00 12%
800.01 - 1200 - 10%
1200.01-2000 - 7%
Acima de 2000 - 4%
"""

salario = float(input("Digite o seu salário: "))

if salario <= 400.00:
    percentual = 15
elif salario <= 800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

reajuste_percentual = salario * (percentual/100)
novo_salario = salario + reajuste_percentual

print(f"Novo Salário: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste_percentual:.2f}")
print(f"Em percentual: {percentual} %")