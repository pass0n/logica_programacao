#Algoritmo: Laço For III

import random

while True:
    aleartorioMaximo = random.randint(1, 100)
    aleartorioMinimo = random.randint(1, 100)
    
    if aleartorioMaximo >= aleartorioMinimo:
        print("maximo:", aleartorioMaximo)
        print("minimo:", aleartorioMinimo)
        break
    
incremento = random.randint(1, 5)
print("incremento:", incremento)

for i in range(aleartorioMinimo, aleartorioMaximo, incremento):
    print(i)