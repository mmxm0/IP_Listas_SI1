class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.a = ladoA
        self.b = ladoB
        self.c = ladoC

    def calculaPerimetro(self,a,b,c):
        self.perimetro = a + b + c
        return self.perimetro
    
    def getMaiorLado (self,a,b,c):
        if a < b and a < c:
            self.maiorlado = a
            return self.maiorlado
        if b<a and b<c:
            self.maiorlado = b
            return self.maiorlado
        else:
            self.maiorlado = c
            return self.maiorlado
