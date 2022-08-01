print("PREENCHA OS DADOS ABAIXO PARA CALCULAR SEU IMC:")

alt = float(input("Altura: "))
peso = float(input("Peso: "))

IMC = peso / (alt * alt)

if IMC < 18.5:
    print("Abaixo do peso!")
elif (IMC >= 18.6) and (IMC <= 24.9):
    print("Saudável!")
elif (IMC >= 25) and (IMC <= 29.9):
    print("Peso em excesso!")
elif (IMC >= 30) and (IMC <= 34.9):
    print("Obesidade Grau I")
elif (IMC >= 35) and (IMC <= 39.9):
    print("Obesidade Grau II (severa)!")
elif IMC >= 40:
    print("Obesidade Grau III (mórbida)!")
