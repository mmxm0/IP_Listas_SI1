'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares
e a quantidade de números impares.
'''
x = 0
pares = 0
impares = 0
while (x <10):
    numero = int(input("informe um número inteiro: "))
    x +=1
    if (numero%2 == 0):
        pares +=1
    else:
        impares +=1
print("Você informou %i numeros pares e %d numeros impares." %(pares,impares))
