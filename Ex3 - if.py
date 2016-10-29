'''
Entrar com um distância (km) e  o tempo de viagem (horas) de um automóvel,
e dizer se a velocidade média foi superior ao limite (110 km/h) ou não.
'''
velocidade = 0
distancia = float(input("Digite a distância percorrida (Km): "))
tempo = float(input("Digite o tempo de viagem(horas): "))

velocidade = distancia/tempo

if velocidade > 110:
    print("A velocidade média foi superior ao limite de 110 km/h")
else:
    print("A velocidade está dentro do limite =) ")
