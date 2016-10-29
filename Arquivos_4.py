'''Crie um programa que leia um arquivo com uma lista de nomes de um arquivo e só
deixe os nomes que iniciam com vogal no mesmo arquivo.
Nome1
Nome2
Nome3 etc'''
lista = ''

ler = open('nomes.txt', 'r')
leitura = ler.readlines()
ler.close()
for i in leitura:
    if i[0] in "AEIOU":
        lista +=i
escrever = open('nomes.txt', 'w')
escrever.write(lista)
escrever.close()