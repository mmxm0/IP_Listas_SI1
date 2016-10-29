'''
Created on 22 de set de 2015

@author: cleviton
'''
temperMeses = [15, 16, 20, 24, 34, 36, 37,40, 35, 24, 20, 23]
nomeMeses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

media = sum(temperMeses) / len(temperMeses)
print("Média: %.2f" % media)

cont = 0
while cont < len(temperMeses):
    if(temperMeses[cont] > media):
        print(nomeMeses[cont])
    cont += 1
