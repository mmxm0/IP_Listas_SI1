'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido. '''

numero = int(input("Digite o numero para saber o dia correspondente da semana (de 1 à 7): "))
if numero == 1:
    print("Domingo")
if numero == 2:
    print("Segunda")
if numero == 3:
    print("Terça")
if numero == 4:
    print("Quarta")
if numero == 5:
    print("Quinta")
if numero == 6:
    print("Sexta")
if numero == 7:
    print("Sábado")
if numero>7 or numero<1:
    print("Valor inválido")
input("pressione ENTER para sair...")
    
