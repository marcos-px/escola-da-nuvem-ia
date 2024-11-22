#Programa em Python que calcula a sequencia de Fibonnaci

def fibonnaci(n):

    """
    Gerar a série de Fibonacci (lógica) até o N-esimo termo
    """

    #Iniciar os primeiros valores da série
    a, b = 0 , 1
    resultado = [a]

    #Geração de termo (É a lógica por trás da resolução do problema)
    for _ in range(1, n):
        resultado.append(b)
        a, b = b, a + b

    #Função devolve o resultado: [0,1,1,2,3]
    print(f"Resultado sem tratamento: {resultado}")
    return resultado
    

def main():
    try:
        N = int(input())

        if N <= 0 or N >= 46:
            raise ValueError(" O número precisa estar entre 1 e 45")
        
        #Pega o resultado sem tratar: [0,1,1,2,3,5]
        fibonnaci_sequence = fibonnaci(N)

        #Pega o resultado tratado:

        print(" ".join(map(str, fibonnaci_sequence)))
    
    except ValueError as ve:
        print(f"Erro {ve}")

if __name__ == "__main__":
    main()
