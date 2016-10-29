'''Crie um programa que receba do usuário o tamanho de uma matriz e por fim crie
uma matriz identidade. '''
z = 0

matriz = []
x = int(input("Informe o tamanho da matriz: "))

for i in range(x):
    matriz.append([0]*x)
    matriz[i][i] = 1

print("Matriz identidade de %i x %i : " % (x, x))
print()
while z < x:

    for i in range(x):
        print(matriz[z][i], end=" ")
    z += 1
    print()
