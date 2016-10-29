'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
nTermo= int(input("Informe quantos termos deseja que sua série tenha..."))
n1=1
n2=1
serie = 1
x = 2
print(n1)
print(n2)
while x < nTermo:
    serie= n1+n2
    n1 = n2
    n2 = serie
    print(serie)
    x +=1
