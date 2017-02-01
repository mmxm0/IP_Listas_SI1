'''1- Os alunos da cadeira de Taxonomia do curso de biologia precisam
de um sistema que cadastre os nomes dos seres vivos que estudam de acordo
com os seguintes parâmetros: nome vulgar ou nome comum e o nome cientifico.
O nome cientifico de um ser vivo obedece as seguintes regras: é um nome composto
por dois nomes em latim, sendo o primeiro indicando o gênero e o segundo nome
indicando a espécie. Desenvolva esse sistema. Ele deve conter um método que
faça o nome cientifico ser válido, isto é: o primeiro nome deve sempre começar
com letra  maiúscule e o segundo e com letra minúscula.
Adicione também metódos que obetenha o gênero e a espécie do ser vivo.
Teste sua classe.
'''
class SeresVivos:
    def __init__(self, seres=[]):
        self.__seres = []

    def adicionaSer(self, ser):
        self.__seres.append(ser)
            
    def getSeres(self):
        for i in self.__seres:
            print("Nome: %s \nNome Cientifico: %s"%(i.getNomeComum(),i.getNomecientifico()))
        
        
class Ser:
    def __init__(self, nome_vulgar, nome_cientif):
        self.__nome = nome_vulgar
        self.__cientifico = nome_cientif

    def validaNome(self):
        nome = self.__cientifico
        if nome.count(" ") == 1:
            nomes = nome.split()
            n1 =nomes[0].title()
            n2= nomes[1].lower()
            nome = n1+" "+n2
            self.__cientifico = nome
            
        else:
            print("nome invalido")
        
    def getNomecientifico(self):
        return self.__cientifico

    def getNomeComum(self):
        return self.__nome
    def cadastraNome(self, novonome):
        self.__nome = novonome

    def cadastraNomeCientifico(self, novonome):
        self.__cientifico = novonome
        
    def genero(self):
        nome = self.__cientifico
        if " " in nome:
            nomes = nome.split()
            return nomes[0]
        else:
            print("nome inválido")

    def especie(self):
        nome = self.__cientifico
        if " " in nome:
            nomes = nome.split()
            return nomes[1]
        else:
            print("nome inválido")        

ser1 = Ser("argan", "Argania Spinalis")
ser1.validaNome()
print(ser1.getNomecientifico())
print(ser1.getNomeComum())
print("Genero: %s \nEspecie: %s"%(ser1.genero(), ser1.especie()))
conjunto= SeresVivos()
conjunto.adicionaSer(ser1)
conjunto.getSeres()
