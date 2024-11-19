try:
    idade = int(input("Digite a sua idade: "))
    if idade <0:
        raise ValueError("Idade não pode ser negativa")
    print(f"Sua idade é: {idade}")
except ValueError as error:
    print(f"Erro: {error}")