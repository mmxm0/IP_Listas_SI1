#Faça um programa que receba dois números inteiros e gere os
#números inteiros que estão no intervalo
#compreendido por eles

numero1 = int(input("Digite o primeiro numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))
for i in range(numero1,numero2):
    if (i != numero1)and (i != numero2):
        print(i)
    
