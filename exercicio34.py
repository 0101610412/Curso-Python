print("Insira a nota e o número de faltas do aluno para obter seu conceito:")
nota = float(input("Nota: "))
faltas = int(input("Nº de faltas: "))

if (nota > 9.0) and (nota <= 10.0):
    if (faltas > 1) and (faltas < 20):
        print("Conceito: A")
    elif faltas > 20:
        print("Conceito: B")
elif (nota > 7.5) and (nota <= 8.9):
    if (faltas > 1) and (faltas < 20):
        print("Conceito: B")
    elif faltas > 20:
        print("Conceito: C")
elif (nota > 5.0) and (nota <= 7.4):
    if (faltas > 1) and (faltas < 20):
        print("Conceito: C")
    elif faltas > 20:
        print("Conceito: D")
elif (nota > 4.0) and (nota <= 4.9):
    if (faltas > 1) and (faltas < 20):
        print("Conceito: D")
    elif faltas > 20:
        print("Conceito: E")
elif (nota >= 0.0) and (nota <= 3.9):
    if (faltas > 1) and (faltas < 20):
        print("Conceito: E")
    elif faltas > 20:
        print("Conceito: E")
