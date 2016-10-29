'''Faça um programa que imprima o fatorial de um número.
O valor de entrada deve ser menor ou igual a 20.'''
x =1
resultado = 1
fatorial = int(input("Informe o número que deseja o fatorial (até 20): "))
if fatorial <=20:
    while x <=fatorial:
        resultado= resultado*x
        x +=1
    print(fatorial,"! = %d " %resultado)
else:
    print("Valor inválido")

input("Pressione ENTER para sair...")
