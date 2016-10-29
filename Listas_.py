
lista = [1,2,3,4,5,6]
votos = []
print("Informe o valor do seu voto:")
print("1 - Windows")
print("2 - Unix")
print("3 - Linux")
print("4 - Netware")
print("5 - Mac")
print("6 - Outros")
valor = int(input("Informe o numero correspondente ao seu voto: "))
while True:
    if valor == 0:
        print("program finished")
        break
    if valor in lista:
        votos.append(valor)
        print("Informe o valor do seu voto:")
        print("1 - Windows")
        print("2 - Unix")
        print("3 - Linux")
        print("4 - Netware")
        print("5 - Mac")
        print("6 - Outros")
        valor = int(input("Informe o numero correspondente ao seu voto: "))
    else:
        print("valor inválido!")
        print("Informe o valor do seu voto:")
        print("1 - Windows")
        print("2 - Unix")
        print("3 - Linux")
        print("4 - Netware")
        print("5 - Mac")
        print("6 - Outros")
        valor = int(input("Informe o numero correspondente ao seu voto: "))

totalVotos = len(votos)
windows = votos.count(1)
percWin = windows/totalVotos*100
unix = votos.count(2)
percUnix = unix/totalVotos*100
linux = votos.count(3)
percLinux = linux/totalVotos*100
netware = votos.count(4)
percNet = netware/totalVotos*100
mac = votos.count(5)
percMac = mac/totalVotos*100
outros = votos.count(6)
percOutros = outros/totalVotos*100
print('{:-<15}'.format("Sistema Operacional    Votos   % "))
print('{:-<15}'.format("-------------------   ------ -----"))
print('{:-<15}'.format("Windows                %i     %.1f" % (windows, percWin), "%"))
print('{:-<15}'.format('Unix                   %i     %.1f' % (unix, percUnix), "%"))
print('{:-<15}'.format("Linux                  %i     %.1f" % (linux, percLinux), "%"))
print('{:-<15}'.format("Netware                %i     %.1f" % (netware, percNet), "%"))
print('{:-<15}'.format("Mac                    %i     %.1f" % (mac, percMac), "%"))
print('{:-<15}'.format("Outros                 %i     %.1f" % (outros, percOutros), "%"))
print('{:-<15}'.format("------------ -----"))
print('{:-<15}'.format("Total         %i votos" % (len(votos))))
input()