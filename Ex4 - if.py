
'''Faça um Programa que peça para entrar com um ano (inteiro com 4 dígitos)
e determine se o mesmo é ou não bissexto (divisível por 4).'''
ano = int(input("digite o ano para saber se ele é bissexto: "))
if ano%4 == 0:
    print(ano, ' eh um ano bissexto' )
else:
    print(ano, ' NO eh um ano bissexto')
input()

