'''
Crie um algoritmo que lê um conjunto de nomes de um arquivo ‘nomes.txt’. Esse
algoritmo deverá separar os nomes que iniciam com vogal e escrever em um novo
arquivo ‘vogal.txt’, enquanto que os nomes que iniciam com consoante devem ser
escritos no arquivo ‘consoante.txt’.
'''
arquivonome = open('nomes.txt', 'r')
lista = arquivonome.readlines()
arquivoconsoante = open("consoante.txt", 'w')
arquivovogal = open('vogal.txt', 'w')

print(lista)
for i in lista:
    if i[0] in "AEIOU":
        arquivovogal.write(i)
    else:
        arquivoconsoante.write(i)
arquivoconsoante.close()
arquivonome.close()
arquivovogal.close()
