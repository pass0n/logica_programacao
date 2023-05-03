 #Algoritmo: While III
 
maisNovo = 9999
maisVelho = 0
qtdEntrevistados = 0
qtdMenoresIdade = 0
somaIdades = 0
 
while qtdEntrevistados < 5:
    idadeInformada = int(input("Favor, informe a sua idade: "))
     
    if idadeInformada > maisVelho:
        maisVelho = idadeInformada
        
    if idadeInformada < maisNovo:
        maisNovo = idadeInformada
        
    if idadeInformada < 18:
         qtdMenoresIdade += 1
     
    somaIdades = somaIdades + idadeInformada    
    qtdEntrevistados += 1
    
print(f"Mais novo: {maisNovo}")
print(f"Mais velho: {maisVelho}")
procentagemMenorIdade = (qtdMenoresIdade / 5 ) * 100
print(f"Porcentagem menor idade:  {procentagemMenorIdade}%")
mediaIdade = somaIdades / 5
print(f"Media de idade {mediaIdade}")        
 