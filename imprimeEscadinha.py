'''
http://wiki.python.org.br/ExerciciosFuncoes
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''
def imprimeEscadinha (n):
    x= 1
    for i in range(1,n+1):
        for j in range(i):
            print(i, end="  ")
        print()
n = int(input("Informe um valor inteiro para ser impresso em forma de 'escada':"))

print(imprimeEscadinha(n))
