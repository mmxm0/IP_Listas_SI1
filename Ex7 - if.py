'''Faça um Programa que pergunte em que turno a pessoa estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso. '''

turno = input("Em qual turno você estuda? (Digite M para Matutino, V para Vespertino e N para Noturno): ")
if turno == "M":
    print("Bom dia!")
if turno == "V":
    print("Boa Tarde!")
if turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
    
