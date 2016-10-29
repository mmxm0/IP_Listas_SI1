'''
Created on 22 de set de 2015

@author: cleviton
'''
#Primeira maneira de resolver
numeros = [1,2,4,7,8,45,36,78,98,13,54,56,76,45,34,76,94,24,10,12]
pares = []
impares = []
for num in numeros:
    if(num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)
print("Pares: %s" % pares)
print("Impares: %s" % impares.__str__())

#Segunda maneira de resolver
novosPares = [x for x in numeros if x % 2 == 0]
novosImpares = [i for i in numeros if i % 2 != 0]
print("Novos Pares: %s" % novosPares.__str__())
print("Novos Impares: %s" % novosImpares.__str__())