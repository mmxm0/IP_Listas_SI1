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
print(conjunto.getSeres())
