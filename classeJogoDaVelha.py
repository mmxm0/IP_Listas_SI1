class JogoDaVelha:
    def __init__(self, jogadorInicial = "X"):
        self.matriz = []
        self.vencedor = None
        self.jogador = jogadorInicial
        self.InicializaMatriz()
        self.qtdeJogadas = 0
        self.ativo = True

    def InicializaMatriz(self):
        self.matriz = [["_", "_", "_"], ["_", "_", "_"],["_", "_", "_"]]
    def getStrGrade(self):
        grade = ""
        ultimaLinha = [" ", " ", " "]
        if self.matriz[2][0] != "_":
            ultimaLinha[0] = self.matriz[2][0]
        if self.matriz[2][1] != "_":
            ultimaLinha[1] = self.matriz[2][1]
        if self.matriz[2][2] != "_":
            ultimaLinha[2] = self.matriz[2][2]
        grade+="L      C O L U N A S\n"
        grade+="I      1     2     3\n"
        grade+="N  1 __%s__|__%s__|__%s__\n"%(self.matriz[0][0], self.matriz[0][1], self.matriz[0][2])
        grade+="H  2 __%s__|__%s__|__%s__\n"%(self.matriz[1][0], self.matriz[1][1], self.matriz[1][2])
        grade+="A  3   %s  |  %s  |  %s  \n"%(ultimaLinha[0], ultimaLinha[1], ultimaLinha[2])
        grade+="S\n"
        return grade
    def getJogadorAtual(self):
        return self.jogador
    def getVencedor(self):
        return self.vencedor
    def getAtivo(self):
        return self.ativo
    def TrocaJogador(self):
        if self.jogador == "X":
            self.jogador = "O"
        else:
            self.jogador = "X"
    def setJogada(self, linha, coluna):
        if self.ativo == True:
            if linha >= 1 and linha <= 3:
                if coluna >=1 and coluna <=3:
                    if self.matriz[linha-1][coluna-1] == "_":
                        self.matriz[linha-1][coluna-1] = self.jogador
                        self.qtdeJogadas += 1
                        self.vencedor = self.VerificaVencedor()
                        if self.vencedor != None: #houve ganhador
                            msg = "P A R A B É N S !!! O JOGADOR '%s' GANHOU O JOGO!!"%self.vencedor
                            self.ativo = False
                        else: #se ninguém ganhou, vamos alternar para o próximo jogador
                            self.TrocaJogador()
                            #verificando se houve empate:
                            if self.qtdeJogadas == 9 and self.vencedor == None:
                                msg = "E M P A T E!!! NÃO HOUVE GANHADOR."
                                self.ativo = False
                            else: #ninguem venceu, jogada normal
                                msg = "OK, PROXIMA JOGADA"
                    else:
                        msg = "Erro! Posição já está preenchida! Tente outra!"
                else:
                    msg = "Coluna inválida! Digite novamente."
            else:
                msg = "Linha inválida! Digite novamente."
        else: #jogo ja tinha terminado, nao precisa fazer nada!
            msg = "Erro! O jogo ja terminou. Voce nao pode jogar mais. Reinicie o jogo."
        return msg #retorna a mensagem

    def VerificaVencedor(self):
        ganhou = None
        #verificando horizontais:
        if self.matriz[0][0] != "_" and self.matriz[0][0] == self.matriz[0][1] and self.matriz[0][1] == self.matriz[0][2]:
            ganhou = self.matriz[0][0]
        elif self.matriz[1][0] != "_" and self.matriz[1][0] == self.matriz[1][1] and self.matriz[1][1] == self.matriz[1][2]:
            ganhou = self.matriz[1][0]
        elif self.matriz[2][0] != "_" and self.matriz[2][0] == self.matriz[2][1] and self.matriz[2][1] == self.matriz[2][2]:
            ganhou = self.matriz[0][0]
        #verificando verticais:
        elif self.matriz[0][0] != "_" and self.matriz[0][0] == self.matriz[1][0] and self.matriz[1][0] == self.matriz[2][0]:
            ganhou = self.matriz[0][0]
        elif self.matriz[0][1] != "_" and self.matriz[0][1] == self.matriz[1][1] and self.matriz[1][1] == self.matriz[2][1]:
            ganhou = self.matriz[0][1]
        elif self.matriz[0][2] != "_" and self.matriz[0][2] == self.matriz[1][2] and self.matriz[1][2] == self.matriz[2][2]:
            ganhou = self.matriz[0][2]
        #verificando diagonal principal:
        elif self.matriz[0][0] != "_" and self.matriz[0][0] == self.matriz[1][1] and self.matriz[1][1] == self.matriz[2][2]:
            ganhou = self.matriz[0][0]
        #verificando diagonal secundária:
        elif self.matriz[2][0] != "_" and self.matriz[2][0] == self.matriz[1][1] and self.matriz[1][1] == self.matriz[0][2]:
            ganhou = self.matriz[2][0]
        return ganhou        
        


#programa principal:
print("J O G O   D A   V E L H A ")
print("JOGADORES: O, X")
jogador = ""
while jogador == "":
    jogador = input("Escolha o jogador que vai começar: ")
    if jogador != "X" and jogador != "O":
        print("Erro! Escolha entre X ou O (maiúsculos)")
        jogador = ""
        
jogo = JogoDaVelha(jogador) #cria o objeto do jogo da velha

#loop das jogadas, repete enquanto o jogo estiver ativo
print(jogo.getStrGrade())
while jogo.getAtivo() == True: 
    jogador = jogo.getJogadorAtual()
    l = int(input("Jogador %s, digite a linha : "%jogador))
    c = int(input("Jogador %s, digite a coluna: "%jogador))
    msg = jogo.setJogada(l, c)
    print(msg)
    print(jogo.getStrGrade())
