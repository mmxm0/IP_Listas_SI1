'''Implemente uma classe Aluno,	que deve ter os
seguintes atributos:	nome,	curso,	tempoSemDormir
(em horas).		Essa classe deverá ter os seguintes
métodos:
– estudar	(que recebe como parâmetro	a	qtd	de	horas	de
estudo	e	acrescenta tempoSemDormir	)
– Dormir	(que recebe como parâmetro	a	qtd	de	horas	de
sono	e	reduz tempoSemDormir	)
Crie	um	código	de	teste	da	classe,	criando	um	objeto
da	classe aluno	e	usando os métodos estudar	e	dormir.	 Ao	final	imprima quanto	tempo	o	aluno está sem
dormir'''


class Alunos:
    def __init__(self, nome, curso, tempoSemDormir):
        self.AlunoNome = nome
        self.CursoNome = curso
        self.TSD = tempoSemDormir

    def estudar(self, qtdHrs):
        tempoSemDormir = self.TSD
        qtdHrs = qtdHrs.split(":")
        tempoSemDormir = tempoSemDormir.split(":")
        qtdHrs = [int(x) for x in qtdHrs]
        tempoSemDormir = [int(z) for z in tempoSemDormir]
        tempoSemDormir[0] += qtdHrs[0]
        mod = qtdHrs[1] + tempoSemDormir[1]
        tempoSemDormir[0] += mod // 60
        tempoSemDormir[1] = mod % 60
        tempoSemDormir[1] = "%.2d" % tempoSemDormir[1]
        tempoSemDormir = [str(z) for z in tempoSemDormir]
        tempoSemDormir = ':'.join(tempoSemDormir)
        return tempoSemDormir

    def dormir(self, qtdhorassono):
        tempoSemDormir = self.TSD
        qtdhorassono = qtdhorassono.split(":")
        tempoSemDormir = tempoSemDormir.split(":")
        tempoSemDormir = [int(z) for z in tempoSemDormir]
        qtdhorassono = [int[y] for y in qtdhorassono]
        tempoSemDormir[0] -= qtdhorassono[0]




marta = Alunos("Marta", "BSI", "10:56")
horaatualizada = marta.estudar('6:30')
#horadormir = marta.dormir("3:30")
print(horaatualizada)
#print(horadormir)
