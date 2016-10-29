'''
http://wiki.python.org.br/ExerciciosFuncoes

Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''
def PositivoOuNegativo(argumento):
    i = " "
    if argumento <= 0:
        i = "N"
    else:
        i="P"
    return i

argumento = float(input("Informe um número: "))
print(PositivoOuNegativo(argumento))
