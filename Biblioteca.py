from Livro import Livro
class Biblioteca:

    def __init__(self):
        self.__listaAlugados = []
        self.__listaDisponiveis = []

    def alugar(self, livrodesejado):
        podealugar = False
        for livro in self.__listaDisponiveis:
            if livro.getTitulo() == livrodesejado:
                self.__listaDisponiveis.remove(livro)
                self.__listaAlugados.append(livro)
                podealugar = True
                break
        if not podealugar:
            print("Esse livro não se encontra na relação de Livros Disponiveis")

    def devolver(self, livrodevolvido):
        for livro in self.__listaAlugados:
            if livro.getTitulo() == livrodevolvido:
                self.__listaAlugados.remove(livro)
                self.__listaDisponiveis.append(livro)
                print("Livro devolvido com sucesso")

    def setLivro(self, livro):
        self.__listaDisponiveis.append(livro)

    def getDisponiveis(self):
        print(self.__listaDisponiveis)

    def getIndiponivel(self):
        print(self.__listaAlugados)

biblioteca = Biblioteca()
livro1 = Livro("Bestiario", "julio cortazar", "0022002", 243)
biblioteca.setLivro(livro1)
livro2 = Livro("O senhor do aneis", "J.R.R. Tolkien", "0920329", 698)
biblioteca.setLivro(livro2)
livro3 = Livro("O Hobbit", "J.R.R. Tolkien", "093890292", 500)
biblioteca.setLivro(livro3)
