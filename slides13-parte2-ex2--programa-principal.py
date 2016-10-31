from slides13parte2ex2 import *
#importou as classes Biblioteca e Livro

def imprimeMenu():
    print()
    print("----------------------------------------------")
    print("::   Bem vindo 'a biblioteca da U F R P E   ::")
    print("::   Por favor, selecione a opcao desejada: ::")
    print("::   1. Cadastrar um livro                  ::")
    print("::   2. Alugar um livro                     ::")
    print("::   3. Devolver um livro                   ::")
    print("::   4. Exibir o livro mais alugado         ::")
    print("::   5. Sair do sistema                     ::")
    print("--------------------------------------------::")
    print(":::::: Digite a sua opcao: ")
    return input()

#programa principal:
bib = Biblioteca()
sair = False

while sair == False:
    op = imprimeMenu()
    if op == "5":
        sair = True
    elif op == "1": #inserir um livro
        tit = input("Digite o titulo do livro: ")
        aut = input("Digite os autores do livro: ")
        l = Livro(tit, aut)
        bib.inserirLivro(l)
    elif op == "2": #alugar
        cod = int(input("Digite o codigo do livro que deseja ALUGAR: "))
        bib.alugarLivro(cod)
    elif op == "3": #devolver
        cod = int(input("Digite o codigo do livro que deseja DEVOLVER: "))
        bib.devolverLivro(cod)
    elif op == "4": #livro mais alugado
        bib.livroMaisAlugado()
    else:
        print("Erro! Opcao invalida! Voce deve escolher uma opcao entre 1 e 5")
    












