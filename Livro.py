class Livro:
    def __init__(self, titulo, autor, ID, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__ID = ID
        self.__paginas = paginas


    def getTitulo(self):
        return self.__titulo

    def __repr__(self):
        return "Titulo: %s - Autor: %s" % (self.__titulo, self.__autor)
