
'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

qtdprestacoes = 0
apuracao = 0.0


def valorPagamento(valorPrestacao, diasDeAtraso):
    if diasDeAtraso > 0:
        valoraSerPago = valorPrestacao * 0.03
        juros = diasDeAtraso * 0.001
        valoraSerPago = valoraSerPago + juros + valorPrestacao
               
    else:
        valoraSerPago = valorPrestacao

    return valoraSerPago


while True:
    valorPrestacao = float(input('Informe o valor da prestação: '))
    if valorPrestacao == 0:
        break
    qtdprestacoes += 1
    diasDeAtraso = float(input("Informe os dias de atraso (se não houver atraso informe '0'): "))
    retornovalorpagamento = valorPagamento(valorPrestacao, diasDeAtraso)
    apuracao += retornovalorpagamento
    print("Valor a ser pago pela sua fatura é %.2f" %retornovalorpagamento)

print("Relatório do dia\nQuantidade de prestações: %i\nValor total de prestações pagas no dia: %.2f" %(qtdprestacoes, apuracao))
