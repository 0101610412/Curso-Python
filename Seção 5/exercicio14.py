TL = float(input("Nota do Trabalho de Laboratório: "))
AS = float(input("Nota da Avaliação Semestral: "))
EF = float(input("Nota do Exame Final: "))

TrabLab = 2
AvSem = 3
ExFinal = 5

Mp = (TrabLab*TL + AvSem*AS + ExFinal*EF) / (TrabLab + AvSem + ExFinal)
print("Média do aluno: ", "%.1f" % Mp)

if (Mp > 0.0) and (Mp < 2.9):
    print("Situação: Reprovado!")
elif (Mp > 3.0) and (Mp < 4.9):
    print("Situação: Recuperação!")
elif (Mp > 5.0) and (Mp < 10.0):
    print("Situação: Aprovado!")
