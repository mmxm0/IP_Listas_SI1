class Livro:
    def __init__(self, titulo, autores, codigo=0):
        self.titulo = titulo
        self.autores = autores
        self.codigo = codigo
        self.qtdealugueis = 0
    def aumentaQtdeAlugueis(self):
        self.qtdealugueis += 1
    def getQtdeAlugueis(self):
        return self.qtdealugueis
class Biblioteca:
    qtdeLivros = 0
    def __init__(self):
        self.alugados = []
        self.disponiveis = []
    def inserirLivro(self, novoLivro):
        self.qtdeLivros += 1
        novoLivro.codigo = self.qtdeLivros
        self.disponiveis.append(novoLivro)
    def alugarLivro(self, codigo):
        #procurar se o codigo pertence a algum livro na lista disponiveis
        for i in range(len(self.disponiveis)):
            if self.disponiveis[i].codigo == codigo: #achou
                l = self.disponiveis.pop(i) #retira o livro da lista disponiveis
                l.aumentaQtdeAlugueis()
                self.alugados.append(l) #coloca o livro de alugados
                print("O livro %s foi alugado com sucesso! :)"%(l.titulo))
                break
        else:
            for l in self.alugados: #verificando se o livro desejado esta ja esta alugado:
                if l.codigo == codigo: #achei!
                    print("Erro! O livro ja esta alugado!!")
                    break
            else:
                print("Erro! O codigo informado nao existe na base de dados.")

    def devolverLivro(self, codigo):
        #procurar se o livro esta alugado:
        for i in range(len(self.alugados)):
            if self.alugados[i].codigo == codigo: #achou
                l = self.alugados.pop(i)
                self.disponiveis.append(l)
                print("O livro %s foi devolvido com sucesso! :)"%(l.titulo))
                break
        else:
            #verificando se o livro NAO esta alugado
            for l in self.disponiveis:
                if l.codigo == codigo: #achei! esta disponivel, nao pode devolver um livro que nao esta alugado
                    print("Erro! Voce esta tentando devolver um livro que nao esta alugado.")
                    break
            else:
                print("Erro! O codigo informado nao existe na base de dados.")

    def livroMaisAlugado(self):
        maior = 0
        livroMaisAlugado = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                livroMaisAlugado = livro
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                livroMaisAlugado = livro
        if maior == 0:
            print("Erro! Nenhum livro foi alugado ainda...")
        else:
            print("O livro mais alugado foi %s com %d alugueis."%(livroMaisAlugado.titulo, maior))

    
