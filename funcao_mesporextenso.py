'''
Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato D de mesPorExtenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

meses = [None,"Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

def mesPorExtenso(data, meses):
    mes = data[3:5]
    dia = data[0:2]
    ano = data[6:10]
    mesCorrespondente = int(mes)
    for i in meses:
        if meses.index(i) == mesCorrespondente:
            print("  %s de %s de %s" % (dia, i, ano))


data = input("Informe uma data no formato DD/MM/AAAA:")
mesPorExtenso(data, meses)
