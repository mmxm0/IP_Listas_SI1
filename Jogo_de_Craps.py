
'''
Jogo de Craps.
Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
from random import choice
lista1 = [1,2,3,4,5,6]
lista2 = lista1[:]
pontos = [4,5,6,8,9,10]
contadorJogadas = 0
ponto = 0
def jogaDados(lista1, lista2):
    dado1 = choice(lista1)
    dado2 = choice(lista2)
    result = dado1 + dado2
    
    return result


def encontrapontonovamente(ponto, contadorJogadas, valorDado):
    
    if valorDado == 7:
        print("Você tirou 7 e perdeu :(")
        
    while valorDado != 7:
        valorDado = jogaDados(lista1, lista2)
        print('Os dados rolaram e juntos deram: %i' %valorDado)
        contadorJogadas +=1
        if ponto == valorDado:
            print("Você jogou os dados %i vezes \nTirou %i e ganhou!!!" %(contadorJogadas, valorDado))
            break
        
    
        

    
while True:
    jogada = input("Quer jogar Craps? [S/N]: ")
    jogada = jogada.upper()
    if jogada == 'N':
        break
    valorDado = jogaDados(lista1, lista2)
    print('Os dados rolaram e juntos deram: %i' %valorDado)
    if valorDado == 7 or valorDado == 11:
        print("Você é um natural e ganhou!")
        break
    
    if valorDado == 2 or valorDado == 3 or valorDado == 12:
        print("CRAPS você perdeu!")
        break
    for i in pontos:
        if i == valorDado:
            contadorJogadas += 1
            ponto = i
            encontrapontonovamente(ponto, contadorJogadas, valorDado)
            break
            
    
    
