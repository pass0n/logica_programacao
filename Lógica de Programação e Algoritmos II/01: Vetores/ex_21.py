vetorNomes = []
vetorIdades = []

i = 0

for i in range(5):
    nome = input("Digite o nome: ")
    vetorNomes.append(nome)
    idade = int(input("Digite a idade: "))
    vetorIdades.append(idade)

print(vetorNomes)
print(vetorIdades)