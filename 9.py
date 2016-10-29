'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''

def reverseNumber(n):
    n = str(n)
    return n[::-1]
n = int(input("Informe o numero: "))
reverso = reverseNumber(n)
print("O reverso do numero informado é:", reverso)
