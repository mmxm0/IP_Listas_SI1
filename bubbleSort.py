def bubbleSort(lista, n):
    troca = True
    while troca:
        troca = False
        for i in range( n -1):
            if lista[i] > lista[i+1]:
                chave = lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=chave
                troca = True
    return lista
lista = [99,1,5,4,7,10,34,43,0]
print(lista)
n = len(lista)
print(bubbleSort(lista,n))
