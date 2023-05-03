#algoritmo: Menu

import os

totalConta = 0

while True:
    print("1 - Troca de oleo")
    print("2 - Balanceamento")
    print("3 - Sair")
    
    opcaoMenu = int(input("O que dejesa? "))
    
    os.system("clear")
    
    if opcaoMenu == 1:
        totalConta += 100
    
    if opcaoMenu == 2:
        totalConta += 70
        
    if opcaoMenu == 3:
        print(f"Total conta: R$ {totalConta}")
        break