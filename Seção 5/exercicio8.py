Not1 = float(input("Informe a primeira nota: "))
Not2 = float(input("Informe a segunda nota: "))

Mnota = (Not1 + Not2) / 2

if (Not1 or Not2 > 0.0) or (Not1 or Not2 < 10.0):
    print("Média das notas: ", "%.1f" % Mnota)
else:
    print("Nota Inválida!")
