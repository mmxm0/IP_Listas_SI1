'''
http://wiki.python.org.br/ExerciciosFuncoes

Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(a,b,c):
    return a+b+c


a = int(input("Informe o primeiro numero: "))
b = int(input("Informe o segundo numero: "))
c = int(input("Informe o terceiro numero: "))
print(soma(a,b,c))
