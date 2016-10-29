'''Crie duas listas com números de 0 a 9, embaralhe as listas e sorteie um
número de cada uma para formar uma dezena, repita a operação 5 vezes
para sortear 5 dezenas, assim como na mega sena. Caso a dezena caia como
00 (zero, zero) faça o sorteio dela novamente até sair outra combinação.
Depois disso exiba as dezenas sorteadas.'''
import random
aux = 0

lista1 = ["0","1","2","3","4","5","6","7","8","9"]
lista2 = ["0","1","2","3","4","5","6","7","8","9"]
dezenas= []
dezena = 00
while aux <6:
    n1 = random.choice(list(lista1))
    n2 = random.choice(list(lista2))
    dezena = n1+n2
    if dezenas == "00":
        n2 = random.choice(list(nomes))
        dezena = n1+n2
    dezenas.append(dezena)
    aux +=1
print(dezenas)
input()