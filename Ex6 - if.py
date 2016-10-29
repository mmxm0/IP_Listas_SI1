'''Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato. 
'''
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))
if produto1 < produto2 and produto1< produto3:
    print("Você deve comprar o produto 1, no valor de %.2f, ele é o mais barato" %produto1)
if produto2<produto1 and produto2<produto3:
    print("Você deve comprar o produto 2, no valor de %.2f, ele é o mais barato" %produto2)
else:
    print("Você deve comprar o produto 3, no valor de %.2f, ele é o mais barato" %produto3)
input("press ENTER to exit")
