'''Crie um programa que leia um arquivo no seguinte formato
Nome1 idade1 curso1
Nome2 idade2 curso2
Nome3 idade3 curso3
Armazene os dados lidos em um dicionário e imprima.'''
dic = {}
dados = open("dados.txt", 'r')
listadedados = dados.readlines()
dados.close()


for i in listadedados:
    mo = i.split(" ")

    indice = mo.pop(0)
    dic[indice] = mo
for i in dic:
    print(i," => ",dic[i])
