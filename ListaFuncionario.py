class ListaFuncionario:

    def __init__(self):
        self.__listafuncionario = []

    def insereFuncionario(self, objeto):
        self.__listafuncionario.append(objeto)

    def getLista(self):
        for i in self.__listafuncionario:
            print("%s" % i)
