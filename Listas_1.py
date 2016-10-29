'''
Escreva um programa que solicita 8 inteiros ao usuário e guarda esses valores em
um array. Depois o programa deve descobrir e exibir qual a posição do elemento de
maior valor. 
'''
lista =[]
while len(lista) < 8 :
    inteiros = int(input("Informe um inteiro: "))
    lista.append(inteiros)
print(lista.index(max(lista)))


