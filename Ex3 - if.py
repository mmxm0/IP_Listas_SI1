'''
Entrar com um dist�ncia (km) e  o tempo de viagem (horas) de um autom�vel,
e dizer se a velocidade m�dia foi superior ao limite (110 km/h) ou n�o.
'''
velocidade = 0
distancia = float(input("Digite a dist�ncia percorrida (Km): "))
tempo = float(input("Digite o tempo de viagem(horas): "))

velocidade = distancia/tempo

if velocidade > 110:
    print("A velocidade m�dia foi superior ao limite de 110 km/h")
else:
    print("A velocidade est� dentro do limite =) ")
