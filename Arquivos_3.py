'''Crie um programa que faça criptografia de dados. Ele deve ler um arquivo texto e
gerar um outro arquivo criptografado da seguinte forma: Z->P, R->O, N->L, O->Z,
P->R, L->N onde a primeira deve ser substituída pela segunda. Depois crie um
programa para descriptografar.'''
keys = {"Z": "P", "R": "O", "N": "L", "O": "Z", "P": "R", "L": "N"}
def criptografar(segredoLido, keys):
    string = ""
    for i in segredoLido:
        if i in "ZRNOPL":
            for j in keys:
                if i == j:
                    string += keys[j]
        else:
            string += i
    return string


def descriptografar(mensagemsecreta, keys):
    mensagemdescoberta = ''
    for i in mensagemsecreta:
        if i in "ZRNOPL":
            for j in keys:
                if keys[j] == i:
                    mensagemdescoberta += j
        else:
            mensagemdescoberta += i
    return mensagemdescoberta


segredo = open("arquivo.txt", 'r')
segredoencoberto = open("crypt.txt", 'r+')
revelado = open('reveal.txt', 'w')
segredoLido = segredo.read()
segredoLido = segredoLido.upper()
segredoencoberto.write(criptografar(segredoLido, keys))
mensagemsecreta = criptografar(segredoLido, keys)
revelado.write(descriptografar(mensagemsecreta,  keys))
segredo.close()
segredoencoberto.close()
revelado.close()