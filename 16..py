'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
Faça um programa que gere a série até que o valor seja maior que 500.
'''

n1=1
n2=1
serie = 1

print(n1)
print(n2)
while serie < 500:
    serie= n1+n2
    n1 = n2
    n2 = serie
    print(serie)
    
