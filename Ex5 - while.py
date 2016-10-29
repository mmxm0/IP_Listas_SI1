'''Faça um algoritmo que peça dois números – base e expoente –
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.'''

base = int(input("informe a base: "))
expoente = int(input("informe o expoente: "))
x =1
potencia = base

while x < expoente:
    potencia = base*potencia
    x+=1
    
print(potencia)
