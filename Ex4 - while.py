'''Faça um programa que identifica os 15 primeiros números primos
(utilizando a instrução break). '''

primos = 0
i = 1

while (primos < 16):
    denominador = 2
    while (denominador < i) :
        if(i%denominador == 0):
            break
        denominador += 1
    else:
        primos +=1
        print(i)
    i +=1

intpu("pressione ENTER para sair")
