matricula = int(input("Digite a matrícula do colaborador: "))
horas_trabalhadas = int(input("Digite quantas horas trabalhadas o colaborador teve: "))
valor_hora = float(input("Digite o valor que o colaborador recebe por hora :"))

salario = horas_trabalhadas * valor_hora

print(f"NUMBER = {matricula}")
print(f"SALARY = U$ {salario:.2f}")