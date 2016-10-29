'''
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
potencia = base
x =1
while (x < expoente):
    potencia = potencia*base
    x +=1
print(base,"elevado a",expoente, "é igual a: ", potencia)
