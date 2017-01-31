""" 2 - Houve um época em que, quando as pessoas queriam assistir um filme, iam até a
locadora.
Crie uma classe filme que contém os atributos
gênero, nome, disp_catalogo. Você deve criar um método que altere
a disponibilidade do filme, gets e sets.
Em seguida crie uma classe Locadora, essa classe contém uma lista de todos os
filmes já cadastrados no sistema, crie metodos para listar os
filmes por gênero(Ação, Aventura e Romance), dizer quantos filmes estão alugados(total de todos os filmes),
alugar filmes e devolver.
"""
class Filme:

    def __init__(self, nome,genero,  disp_catalogo=True):
        self.__genero = genero
        self.__titulo = nome
        self.__disponibilidade = disp_catalogo

    def getGenero(self):
        return self.__genero

    def getTitulo(self):
        return self.__titulo

    def getDisponibilidade(self):
        return self.__disponibilidade
    
    def setGenero(self, novo):
        self.__genero = novo

    def setTitulo(self, novo):
        self.__titulo = novo

    def setDisponibilidade(self, novo):
        self.__disponibilidade = novo

    def __str__(self):
        titulo = self.__titulo
        return titulo.title()
    
class Locadora(Filme):
    def __init__(self, filmes=[]):
        self.__filmes = filmes
        self.__alugados = 0
        

    def listaGenero(self, genero):
        print("Filmes de %s\n"%genero)
        for i in self.__filmes:
            if i.getGenero() == genero:
                print(i.getTitulo())

    def listaAlugados(self):
        return "%i filmes alugados "%self.__alugados

    def aluga(self, titulo):
        for i in self.__filmes:
            if i.getTitulo() == titulo and i.getDisponibilidade() == True:
                i.setDisponibilidade(False)
                break
            else:
                print("título indisponível ou invalido")

    def devolve(self, titulo):
        for i in self.__filmes:
            if i.getTitulo() == titulo and i.getDisponibilidade() == False:
                i.setDisponibilidade(True)
                break
            else:
                print("título disponível ou invalido")


    def setFilme(self, novo):
        self.__filmes.append(novo)

    def getCatalogo(self):
        for i in self.__filmes:
            print(i)


