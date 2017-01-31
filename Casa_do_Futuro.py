""" 3 - No futuro, todas as casas serão inteligentes, com sistemas automáticos para
abrir e fechar portas e janelas, acender e apagar luzes das áreas externas e etc.
Crie uma classe Casa que contenha os atributos: portas, janelas,
luz_externa, luz_interna. As portas e janelas devem abrir e fechar, e a luz externa
deve ser ligada automaticamente dependendo da hora informada (liga às 18:00
e desliga às 3:00hrs). Teste sua classe.
"""

class Casa:
    def __init__(self):
        self.__portas = None
        self.__janelas = None
        self.__luzexterna  = None
        self.__luzinterna = None

    def lightsOn(self):
        self.__luzexterna = True

    def lightsOff(self):
         self.__luzexterna = False
        
    def updateStatusLights(self, time):
        l = time.split(":")
        l = [int(x) for x in l]
        hours = l[0]
        lrange = [18,19,20,21,22,23,0,1,2]
        if hours in lrange:
            self.lightsOn()
            print(self.__luzexterna,"luzes externas acessas")

        if hours in range(3,18):
            self.lightsOff()
            print(self.__luzexterna,"luzes externas não estão acesas")

casa1 = Casa()
casa1.updateStatusLights("2:59")
