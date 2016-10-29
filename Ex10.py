'''
Created on 24 de set de 2015

@author: cleviton
'''
respostas = [0,0,0,0,0]
telefonou = input("Telefonou para a vítima? (s/n) ")
if(telefonou == "s"):
    respostas[0] = 1
local = input("Esteve no local do crime? (s/n) ")
if(local == "s"):
    respostas[1] = 1
mora = input("Mora perto da vítima? (s/n) ")
if(mora == "s"):
    respostas[2] = 1
dividas = input("Tinha dívidas com a vítima? (s/n)")
if(dividas == "s"):
    respostas[3] = 1
trabal = input("Já trabalhou com a vítima? (s/n)")
if(trabal == "s"):
    respostas[4] = 1

soma = sum(respostas)

classif = ""
if(soma < 3):
    classif = "suspeito"
elif(soma > 2 and soma <= 4):
    classif= "cúmplice"
elif(soma == 5):
    classif = "assassino"
elif(soma < 2):
    classif = "inocente"
print("A classificação é %s" % classif)