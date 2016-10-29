'''Crie um programa que leia dois arquivos e crie um terceiro com um merge do
conteúdo dos dois'''
juntando = ''
i = 0
arquivo1 = open('arquivo1.txt', 'r')
arquivo2 = open('arquivo2.txt', 'r')
merge = open('merge.txt', 'w')
leituraarq1 = arquivo1.readline()
leituraarq2 = arquivo2.readline()
juntando = leituraarq1+leituraarq2
merge.write(juntando)
while len(leituraarq1) != 0 or len(leituraarq2) != 0:
    leituraarq1 = arquivo1.readline()
    leituraarq2 = arquivo2.readline()
    juntando = leituraarq1+leituraarq2
    merge.write(juntando)

merge.close()
arquivo2.close()
arquivo1.close()