'''
Created on 24 de set de 2015

@author: cleviton
'''
from random import randint
tamanho = input("Informe o tamanho da matriz: ")
tamanho = int(tamanho)
matriz = []
for i in range(tamanho):
    matriz.append([None]*tamanho)

for linha in range(tamanho):
    for coluna in range(tamanho):
        matriz[linha][coluna] = randint(0, 1000)
print(matriz)