P1 = float(input("Insira a nota da primeira prova: "))
P2 = float(input("Insira a nota da segunda prova: "))
P3 = float(input("Insira a nota da terceira prova: "))

Peso1 = 100.0
Peso2 = 80.0

Mp = (Peso1*P1 + Peso1*P2 + Peso2*P3) / (Peso1 + Peso1 + Peso2)

print("Média do aluno: ", "%.1f" % Mp)

if (Mp > 60.0) or (Mp == 60.0):
    print("Situação: Aprovado!")
elif Mp < 60.0:
    print("Situação: Reprovado!")

