# Algoritmo: Exercícios Condicionais
# acréscimo de 10% = 1.1 || 20% = 1.2 // decréscimo = 0.1

velocidadeLeve = 50 * 1.1
velocidadeMedia = 70
velocidadeGrave = 90
velocidadeGravissima = 110

velocidadeVeiculo = float(input("Escreva a velocidade que o veiculo passou: "))

if velocidadeVeiculo <= velocidadeLeve :
    print("Isento de multa!")
elif velocidadeVeiculo <= velocidadeMedia :
    print("3 pontas na carteira.")
elif velocidadeVeiculo <= velocidadeGrave :
    print("4 pontos na carteira.")
elif velocidadeVeiculo <= velocidadeGravissima :
    print("5 pontos na carteira.")
else :
    print("7 pontos na carteira.")