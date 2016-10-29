'''Crie um programa que leia um arquivo de texto fornecido pelo usuário e crie um
ranking das 5 palavras que mais se repetem (espaço vazio e ‘\n’ não contam)'''
top5 = []
x = 1
contagem = {}
lendo = open('texto.txt', 'r')
arquivo = lendo.read()
arquivo = arquivo.lower()
arquivo = arquivo.replace("\n", " ")
arquivo = arquivo.replace('.', '')
arquivo = arquivo.replace(",", "")
arquivo = arquivo.split(" ")
arquivo.sort()
for i in arquivo:
    palavra = arquivo.count(i)
    contagem[i] = palavra

valorMaisAlto = max(contagem.values())

while valorMaisAlto > 0:
    for word, value in contagem.items():
        if value == valorMaisAlto:
            top5.append("%s => %i " % (word, value))
        if len(top5) == 5:
            break
    valorMaisAlto -= 1
    if len(top5) == 5:
        break

print(top5)
print()