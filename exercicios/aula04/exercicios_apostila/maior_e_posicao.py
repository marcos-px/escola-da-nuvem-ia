import random

# def main():

valor = [random.randint(1,10000) for _ in range(100)]

maior = (max(valor))
posicao = valor.index(maior) + 1

resultado = {
    "Números": valor, 
    "Maior Valor": maior, 
    "Posição": posicao
}

print("\n Números gerados:")
print(valor)
print("\nMaior Valor:", maior)
print("Posiçaõ do Maior Valor: ", posicao)

# if __name__ == "__main__":
# main()