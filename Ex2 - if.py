'''Ler a temperatura de uma pessoa e exibir a mensagem “Febre Alta”
(temp ≥ 39), “Febril” (39 > temp ≥ 37)
ou “Sem Febre” (temp < 37). 
'''

temperatura = int(input("Informe a temperatura (apenas numeros): "))
if temperatura >= 39:
    print("Febre alta")
if 39 > temperatura and temperatura >= 37:
    print("Febril")
else:
    print("Sem febre =)")
input()
