'''
Created on 15 de abr de 2016

@author: cleviton
'''
numeros = [None]*5
for pos in range(5):
    num = int(input("Informe um número: "))
    numeros[pos] = num

for posicao, valor in enumerate(numeros):
    print("%d => %d" % (posicao+1,valor))