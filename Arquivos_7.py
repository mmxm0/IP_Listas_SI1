'''Crie um programa que leia uma matriz 3x3 do usuário e guarde os valores em uma
arquivo, na forma de matriz:
Ex: 1 2 3
    4 5 6
    7 8 9'''
x = 0
matriz = ''
arquivo = open('arquivo.txt', 'w')
linha = 0
coluna = 0
while x < 9:
    while coluna < 3:
        pos = input('Informe o valor da posição na matriz %ix%i: ' %(linha, coluna))
        matriz = matriz+" "+pos
        coluna += 1
        x +=1
    linha +=1
    matriz = matriz+"\n"
    coluna = 0

print(matriz)
arquivo.write(matriz)
arquivo.close()