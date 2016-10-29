'''
Crie uma lista com o nome de 10 pessoas, embaralhe esta lista e sorteie uma
pessoa, depois embaralhe novamente e sorteie outra pessoa, lembrando que
não poderá ser a mesma pessoa a ser sorteada.
'''
import random

nomes= ["Milton","Carolina", "Fagundes", "Carlos", "Lucy", "Vivian", "Martin", "Gabriel", "Fernanda","Rosa"]
sort1 = random.choice(list(nomes))
sort2 = random.choice(list(nomes))
while sort1 == sort2:
    sort2 = random.choice(list(nomes))
print(sort1)
print(sort2)