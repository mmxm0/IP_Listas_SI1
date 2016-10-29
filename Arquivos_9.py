'''Crie um programa que leia um arquivo com vários nomes do usuário e sorteie um
nome aleatório. Após sorteado, o programa deverá escrever um arquivo chamado
vencedor.txt que constará o nome do vencedor.'''

from random import choice

abrir = open('nomes.txt')
abrirsorteado = open('vencedor.txt', 'w')
participantes = abrir.read()
participantes = participantes.replace('\n', ' ')
participantes = participantes.split(' ')
ganhador = choice(list(participantes))
abrirsorteado.write(ganhador)
abrir.close()
abrirsorteado.close()