'''
http://wiki.python.org.br/ExerciciosFuncoes
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.

'''

def somaImposto(taxaImposto, custo):
    taxaImposto = taxaImposto*custo/100
    novocusto = custo + taxaImposto
    return novocusto


custo = float(input("Informe o custo do produto: "))
taxaImposto = float(input("Informe a porcentagem do imposto sobre vendas : "))

print("O valor atulizado do produto é de %.2f" %somaImposto(taxaImposto, custo))
