
'''Fa�a um Programa que pe�a para entrar com um ano (inteiro com 4 d�gitos)
e determine se o mesmo � ou n�o bissexto (divis�vel por 4).'''
ano = int(input("digite o ano para saber se ele � bissexto: "))
if ano%4 == 0:
    print(ano, ' eh um ano bissexto' )
else:
    print(ano, ' NO eh um ano bissexto')
input()

