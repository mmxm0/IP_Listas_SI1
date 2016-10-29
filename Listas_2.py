'''
Escrever um programa que lê 20 números reais e armazena esses valores em um
array. O programa deve calcular a média aritmética dos valores do vetor e imprimir
todos os valores menores do que a média calculada. 
'''
array = []
media= 0.0
while len(array) < 5:
    reais = float(input("Informe o número: "))
    array.append(reais)
media = sum(array)/5

for i in array:
    if i < media:
        print(i)
