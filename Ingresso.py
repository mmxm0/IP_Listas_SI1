class Ingresso:
    def __init__(self, valor):
        self.__preco = valor

    def imprimeValor(self):
        print("R$ %s" % self.__preco)


class IngressoVIP(Ingresso):
    def __init__(self, valor):
        Ingresso.__init__(self, valor)
        self.__preco = valor

    def getValorVIP(self, adicional):
        self.__preco += adicional
        return "R$%.2f" % self.__preco

ingresso1 = Ingresso(20.99)
ingresso2 = IngressoVIP(20.99)
print(ingresso2.getValorVIP(100))
print(ingresso2.imprimeValor())