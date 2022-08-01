h = float(input("Informe a altura: "))
Sexo = input("Informe o sexo (m/f): ")

Masc = (72.7 * h) - 58
Fem = (62.1 * h) - 44.7

if Sexo == 'm':
    print("Peso ideal masculino: ", "%.2f" % Masc)
elif Sexo == 'f':
    print("Peso ideal feminino: ", "%.2f" % Fem)
