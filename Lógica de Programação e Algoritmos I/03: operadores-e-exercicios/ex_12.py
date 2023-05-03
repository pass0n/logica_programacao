#Algoritmo: While

alturaMarcelo = 1.20
alturaJoao = 1.05
crescimentoAnualMarcelo = 0.05
crescimentoAnualJoao = 0.07
idade = 8

while alturaMarcelo >= alturaJoao:
    alturaMarcelo += crescimentoAnualMarcelo
    alturaJoao += crescimentoAnualJoao
    idade += 1
    
print("Idade: ", idade)
print("Altura João: ", round(alturaJoao, 2))
print("Altura Marcelo: ", round(alturaMarcelo, 2))