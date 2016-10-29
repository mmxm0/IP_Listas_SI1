'''10. Crie um programa que abra dois arquivos de texto. Guarde em uma lista as
palavras que aparecem ao mesmo tempo nos dois arquivos. Desconsidere palavras
com menos de 3 caracteres. Salva a lista de palavras em um novo arquivo.'''

lista = []
arquivo1 = open('1.txt')
arquivo2 = open('2.txt')
palavras = open('iguais.txt', 'w')
ler1 = arquivo1.read()
ler1 = ler1.replace("\n", " ")
ler1 = ler1.lower()
ler1 = ler1.split(' ')
ler1.sort()

ler2 = arquivo2.read()
ler2 = ler2.replace("\n", " ")
ler2 = ler2.lower()
ler2 = ler2.split(' ')
ler2.sort()
x = 0

for i in ler1:
    for j in ler2:
        if i == j and i not in lista:
            if len(i) > 3:
                lista.append(i)

for i in lista:
    palavras.write(i)
    palavras.write('\n')

arquivo2.close()
arquivo1.close()
palavras.close()