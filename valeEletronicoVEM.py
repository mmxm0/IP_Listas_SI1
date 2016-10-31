class ValeEletronico:
    __codigo, __nome, __cpf, __saldo = None, None, None, None

    def __init__(self, cod, nome, cpf):
        self.__codigo = cod
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = 0.0
    def CarregarCartao(self, valor):
        if valor > 0:
            self.__saldo += valor

    def VerificarSaldo(self):
        return self.__saldo
    def DebitaDoSaldo(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False
        
class VemEstudante(ValeEletronico):
    __instituicaoEnsino = None
    def __init__(self, cod, nome, cpf, instituicaoEnsino):
        ValeEletronico.__init__(self, cod, nome, cpf)
        self.__instituicaoEnsino = instituicaoEnsino

    def UsarPassagem(self, valorPassagem):
        return self.DebitaDoSaldo(valorPassagem/2.0)
        

class VemTrabalhador(ValeEletronico):
    __empresa = None
    def __init__(self, cod, nome, cpf, empresa):
        ValeEletronico.__init__(self, cod, nome, cpf)
        self.__empresa = empresa

    def UsarPassagem(self, valorPassagem):
        return self.DebitaDoSaldo(valorPassagem)
        
        
            
