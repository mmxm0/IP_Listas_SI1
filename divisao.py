dividendo = int(input())
divisor = int(input())
resultado = 0
resto = 0
while True:
    dividendo -= divisor
    if dividendo >= 0 :
        resultado +=1
    elif dividendo < 0:
        resto += divisor+dividendo
        break
    else:
        print("ERRO: Não se pode dividir por 0")
        break
    
print(resultado)
