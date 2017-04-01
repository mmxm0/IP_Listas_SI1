enesimo = int(input("informe o n-ésimo termo da sequencia: "))
primeiro=0
segundo=1
print(0, end =" ")
cont = 1
while cont < enesimo:
    n = segundo + primeiro
    primeiro = segundo
    segundo = n
    cont+=1
    print(primeiro, end=" ")
    
