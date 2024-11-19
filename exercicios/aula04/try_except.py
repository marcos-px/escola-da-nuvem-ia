try:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    resultado = numero1 / numero2
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Tá errado! Não pode dividir por 0!")
except ValueError:
    print("Pessoa maluca! Operação não permitida!")