from Produto import Produto
class GerenciadorProduto:

    def __init__(self):
        self.__ListaProduto = []

    def AdicionarProduto(self, novoproduto):
        self.__ListaProduto.append(novoproduto)

    def RemoverProduto(self, codigo):
        pos = 0
        for produto in self.__ListaProduto:
            if codigo == produto.getCodigo():
                break
        pos += 1
        return self.__ListaProduto.pop(pos)

    def precoTotal(self, listaProdutos):
        total = 0
        for codigo in listaProdutos:
            for produto in self.__ListaProduto:
                if codigo == produto.getCodigo():
                    total += produto.getPreco()
                    break

        return "Total R$%.2f" %total

