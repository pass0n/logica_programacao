numeros = []
numerosReversos = []

i = 0

for i in range(10):
    num = input("Número: ")
    numeros.append(num)

numerosReversos = numeros[::-1]
    
print(numeros, numerosReversos)