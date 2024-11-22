"""
CIDADE A(SETE LAGOAS) e CIDADE B(OSVALDO CRUZ)
ÍNDICE DE CRESCIMENTO (G1 E G2)
"""

def calculo_anos(PA, PB, G1, G2):
    """
    Função que calcula quantos anos a população de A leva para ultrapassar B
    Se ultrapassar 100 anos, "Mais de 1 século"
    
    """

    anos = 0

    while PA <= PB:
        #Incremento dos anos de forma proporcional multiplicando a porcentagem de G (Indice)
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1


        if anos > 100:
            return "Mais de 1 século" #Dentro do IF
            
    return f"{anos} anos."
    
def main():
    try:
        
        T = int(input()) #numeros de teste

            #[100 400 500 100]
        for i in range (T):
            PA, PB, G1, G2 = map(float, input(). split())
            PA, PB = int(PA), int (PB) #Convertendo Cidades para inteiro

            resultado = calculo_anos(PA, PB, G1, G2)

            print(resultado)

    except ValueError as ve:
        print(f"Erro {ve}")

if __name__ == "__main__":
    main()
