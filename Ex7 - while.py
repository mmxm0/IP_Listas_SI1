'''
Faça o algoritmo de imprimir a tabuada de um número fornecido pelo usuário,
usando while.
Após mostrar a tabuada o programa deve perguntar se deseja imprimir a
tabuada de um novo número.
'''

a=1

while True:
    numero = int(input("Informe o numero que deseja a tabuada: "))    
    while (a<=10):
        print(a,"x",numero,"=",a*numero)
        a +=1
    novo = input("Deseja a tabuada de um novo numero?[S ou N]: ")
    if novo == "N":
        break
    if novo == "S":
        a = 1
    else:
        print("comando inválido!")
        break
