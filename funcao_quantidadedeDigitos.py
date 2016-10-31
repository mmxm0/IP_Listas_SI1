'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

def qtddigitos(n):
    n = str(n)
    return len(n)

n = int(input("Informe um número inteiro: "))
quantidade = qtddigitos(n)
print("O numero informado possui %i digito(s) "  %quantidade)
