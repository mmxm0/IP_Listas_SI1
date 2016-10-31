'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja
ver a tabuada.
'''

numero = int(input("Informe o numero que deseja a tabuada: "))
x=1
while x <=10:
    print(numero," x ",x,"=", x*numero)
    x +=1
