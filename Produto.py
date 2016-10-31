class Produto:
    qtdProd = 0

    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco
        Produto.qtdProd +=1

    def setCodigo(self, novoCodigo):
        self.__codigo = novoCodigo

    def setPreco(self, novoPreco):
        self.__preco = novoPreco

    def getCodigo(self):
        return self.__codigo

    def getPreco(self):
        return self.__preco

    def __repr__(self):
        return "%s - %.2f" % (self.__codigo, self.__preco)

