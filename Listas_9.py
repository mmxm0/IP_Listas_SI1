from random import randint
'''Faça um programa que crie uma matriz aleatoriamente e guarde em uma lista. As
dimensões da matriz deverão ser informadas pelo usuário. O programa deverá
imprimir a matriz criada na tela, no formato m x n. Ex:
Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Exibir na tela:
1 2 3
4 5 6
7 8 9 '''

z = 0

matriz = []
x = int(input("Informe a quantidade de linhas da matriz: "))
y = int(input("Informe a quantidade de colunas da matriz: "))
for i in range(x):
    num = ("%d%d" % (randint(0, 9), randint(0, 9)))
    num2 = ("%d%d" % (randint(0, 9), randint(0, 9)))
    matriz.append([num]*y)
    matriz[i][i] = num2

while z < x:

    for i in range(y):
        print(matriz[z][i], end="  ")
    z += 1
    print()




