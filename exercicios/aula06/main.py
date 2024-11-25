from packages.escola_matematica import operacoes
from packages.contabilidade import juros
import math as m
from datetime import datetime
import random


hora_atual = datetime.now()
print(operacoes.multiplicar(2, 3))
print(juros.calcular_juros_simples(1000, 0.05, 12))
print(m.sqrt(16))
print(f"Hora atual {hora_atual}")
print(random.randint(1,10))