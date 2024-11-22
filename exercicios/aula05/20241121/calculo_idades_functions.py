#Função que calcula as idades

def calcular_media_idades():

    """
    Função, para calcular a média de idades e não considerar a negativa (break)
    
    """

    soma_idades = 0
    quantidade = 0

    while True:
        idade = int(input())

        #Se é negativa ou não
        if idade < 0:
            break

            #Soma as idades
        soma_idades += idade
        quantidade += 1

    #cria o contador de quantidade
    if quantidade > 0:
        media = soma_idades / quantidade
        return f"{media:.2f}"
    else:
        return "Nenhuma idade válida inserida"
    
    #Chama a função de cálculo
def main():
    try:

        media_idades = calcular_media_idades()

        print(media_idades)

    except ValueError:
        print("Erro: entrada inválida, favor enviar números inteiros.")

if __name__ == "__main__":
    main()