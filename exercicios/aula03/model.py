from sklearn.linear_model import LinearRegression
import numpy as np

horas_estudo = np.array([1,2,3,4,5]).reshape(-1,1) #valor referência
notas = np.array([40,50,60,70,80])

#modelo treina
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)

#pergunto ao usuário final
horas = float(input("Digite o número de horas estudadas: "))

#previsão
nota_prevista = modelo.predict([[horas]])

print(f"Com {horas} de estudo, a nota prevista é {nota_prevista[0]:.2f}")