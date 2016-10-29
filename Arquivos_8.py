'''Crie um programa que leia um arquivo e informe a última palavra existente'''

abrir = open('texto.txt', 'r')
ler = abrir.readlines()
ultimafrase = ler[-1]
ultimafrase = ultimafrase.split(' ')
print("a ultima palavra deste arquivo é:\n '%s' " %ultimafrase[-1])

abrir.close()