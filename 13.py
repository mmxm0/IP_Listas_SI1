'''Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.'''


def constroiRetangulo(linhas, colunas):
    retangulo = []
    z = 0

    tamanho = linhas*colunas

    while len(retangulo) < (linhas*colunas):
        retangulo.append("")
    p3 = tamanho - (colunas -1)
    x = colunas + 1

    retangulo[0]= "+"
    retangulo[colunas - 1] ="+"
    retangulo[-1]="+"
    retangulo[tamanho - colunas] = "+"
    for a in range(1, colunas-1):
        retangulo[a] = "-"
    for b in range(p3, tamanho-1):
        retangulo[b] = "-"
    for ladoA in retangulo:
        for c in range(x, )

    for i in range(linhas):
        for j in range(colunas):
            if z < len(retangulo):
                print(retangulo[z], end="")
                z +=1
        print()



linhas = int(input("Informa a quantidade de linhas: "))
colunas = int(input("Informe a quantidade de colunas: "))
constroiRetangulo(linhas, colunas)
