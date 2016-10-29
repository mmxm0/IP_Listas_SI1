'''Escreva um programa que intercale os elementos de duas listas l1 e l2. Exemplo:
para l1 = [1,2,4] e l2 =['a','b','c','d','e'], o programa deve computar a lista
[1,'a',2,'b',3,'c','d','e']
'''

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
l3 = []
x = (len(l1) + len(l2))


while len(l3) < x:
    l3.append(l1.pop(0))
    l3.append(l2.pop(0))

print(l3)