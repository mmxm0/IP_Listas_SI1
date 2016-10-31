class ValeEletronico:
    __codigo,__nome,__cpf,__saldo = None, None, None, None
    
    def __init__(self, cod, nome, cpf):
        
        self.__codigo = cod
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        

    def CarregarCartao (self, valor):
        if valor >0:
            self.saldo  +=valor
            
    def VerificarSaldo (self):
        return self.saldo
    
class VemEstudante(ValeEletronico):
    __instituicaoEnsino = None

    def __init__(self, cod,nome,cpf,instituicaoEnsino, saldo=0.0):
        ValeEletronico.__init__(self, cod, nome, cpf, saldo)
        self.__instituicaoEnsino = instituicaoEnsino

    def usarPassagem(self, valorPassagem):
        if valorPassagem > 0 and valorPassagem/2.0 <= self.saldo:
            self.saldo -= valorPassagem/2.0
            return True
        else:
            return False

class VemTrabalhador(ValeEletronico):
    __empresa = None
    def __init__(self, cod, nome, cpf, empresa, 
            
