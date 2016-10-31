'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
'''

numeroFatorial = int(input("Informe o numero que deseja o fatorial: "))
x = 1
resultado = 1
while (x <= numeroFatorial):
    resultado = resultado*x
    x +=1
print("%d ! é = %i"%(numeroFatorial,resultado))
