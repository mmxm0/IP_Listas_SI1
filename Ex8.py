'''
Created on 24 de set de 2015

@author: cleviton
'''
matriz = []
for i in range(3):
    matriz.append([None]*3)
    
for linha in range(3):
    for coluna in range(3):
        numero = input("Informe o número da posição [%d][%d]: " % (linha, coluna))
        matriz[linha][coluna] = int(numero) * 2
print(matriz)