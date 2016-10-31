from ListaFuncionario import ListaFuncionario

class Funcionario:
    def __init__(self, nome, ponto):
        self.__nome = nome
        self.__ponto = ponto

    def __repr__(self):
        return "%s - %s" % (self.__nome, self.__ponto)

objeto = ListaFuncionario()
funcionarioA = Funcionario("A", "000 000")
objeto.insereFuncionario(funcionarioA)
funcionarioB = Funcionario("B", "001 001")
objeto.insereFuncionario(funcionarioB)
print(objeto.getLista())
