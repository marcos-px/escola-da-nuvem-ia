"""
Qualquer valor entre [0,25], [25,50], [50,75] OU [75,100]]
Preciso incluir os números do intervalo.
"""

entrada = input("Digite um número com no máximo duas casas decimais :")

try:
    numero = float(entrada)
    if '.' in entrada and len(entrada.split('.')[1]) >2:
        print("Erro: O número não pode ter mais de duas casas")
    else:
        numero = round(numero, 2)
        if 0 <= numero <= 25:
            print("Intervalo [0,25]")
        elif 25 < numero <= 50:
            print("Intervalo [25,50]")
        elif 50 < numero <= 75:
            print("Intervalo [50,75]")
        elif 75 < numero <= 100:
            print("Intervalo 75,100")
        else: 
            print ("Fora do Intervalo")
except ValueError:
    print("Erro: Entrada Inválida")