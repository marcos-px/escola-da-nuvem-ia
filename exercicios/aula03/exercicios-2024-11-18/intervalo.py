"""
Qualquer valor entre [0,25], [25,50], [50,75] OU [75,100]]
Preciso incluir os números do intervalo.
"""
#if elif else

numero = round(float(input("Digite um número com no máximo duas casas decimais: ")),2)

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