
saltos = []

media = 0.0
while True:
    atleta = input("Digite o nome do atleta: ")

    if atleta == " ":
        break
    else:
        while len(saltos) < 5:
            alturaSalto = float(input("Informe a altura do salto: "))
            saltos.append(alturaSalto)

        media = sum(saltos)/5



        print("Atleta: %s m"%atleta)
        print("Primeiro Salto: %.1f m"%(saltos[0]))
        print("Segundo Salto: %.1f m"%(saltos[1]))
        print("Terceiro Salto: %.1f m"%(saltos[2]))
        print("Quarto Salto: %.1f m"%(saltos[3]))
        print("Quinto Salto: %.1f m"%(saltos[4]))
        print("Resultado Final: ")
        print("Atleta: %s"%atleta)
        print("Saltos: %.1f m - %.1f m - %.1f m - %.1f m - %.1f m "%(saltos[0],saltos[1],saltos[2],saltos[3],saltos[4]))
        print("Média dos Saltos: %.1f m"%media)

        media = 0.0
        saltos =[]


