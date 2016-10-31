class BombaCombustivel:
    __tipoCombustivel = None
    __valorLitro = None
    __quantidadeCombustivel = None

    def __init__(self, tipoComb="G", valorLitro=3.00, qtdeCombust=0):
        self.__tipoCombustivel = tipoComb
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = qtdeCombust

    def abastecerPorValor(self, valor):
        qtdeLitros = valor / self.__valorLitro
        if qtdeLitros <= self.__quantidadeCombustivel:
            self.__quantidadeCombustivel -= qtdeLitros
            return qtdeLitros
        else:
            return 0 #nao abasteceu -> 0 litros

    def abastecerPorLitro(self, qtdeLitros):
        if qtdeLitros <= self.__quantidadeCombustivel:
            self.__quantidadeCombustivel -= qtdeLitros
            #calculando o preço:
            return qtdeLitros * self.__valorLitro
        else:
            return 0 #nao abasteceu -> 0 reais

    def alterarValor(self, novoPreco):
        self.__valorLitro = novoPreco

    def alterarCombustivel(self, novoTipo):
        self.__tipoCombustivel = novoTipo

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.__quantidadeCombustivel = novaQuantidade

    def getQuantidadeCombustivel(self):
        return self.__quantidadeCombustivel
    
    def getTipoCombustivel(self):
        return self.__tipoCombustivel

    def getValorLitro(self):
        return self.__valorLitro

##>>> 
##>>> b = BombaCombustivel("A", 2.30, 5000)
##>>> b.abastecerPorValor(100)
##43.47826086956522
##>>> b.getQuantidadeCombustivel()
##4956.521739130435
##>>> b.getTipoCombustivel()
##'A'
##>>> b.getValorLitro()
##2.3
##>>> b.__valorLitro
##
##Traceback (most recent call last):
##  File "<pyshell#21>", line 1, in <module>
##    b.__valorLitro
##AttributeError: BombaCombustivel instance has no attribute '__valorLitro'
##>>> 
