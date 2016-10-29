'''Faça um programa que peça 5 valores positivos do usuário
(usando while). Caso o usuário digite algum número negativo
o programa deve terminar imediatamente.
Caso termine normalmente informe que os dados foram inseridos com sucesso
(use o else).'''
x= 0
while (x < 5) :
    valor = int(input("Digite um valor: "))
    if valor < 0:
        break
    
    x +=1
else:
    print("Os dados foram inseridos com sucesso! ")
input("pressione ENTER para sair")
