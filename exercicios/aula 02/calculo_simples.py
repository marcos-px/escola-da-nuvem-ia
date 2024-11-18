cod1, qtd1, valor1 = input(" Digite o código, quantidade e valor do primeiro item: ").split()
cod2, qtd2, valor2 = input(" Digite o código, quantidade e valor do segundo item: ").split()

qtd1, valor1 = int(qtd1), float(valor1)

qtd2, valor2 = int(qtd2), float(valor2)

valor_total = (qtd1 * valor1) + (qtd2 * valor2)

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
