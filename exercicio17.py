print("Para descobrir a área de um trapézio indique:")
BMA = float(input("Sua base maior (número menor que 0 não será aceito): "))
Bme = float(input("Sua base menor: "))
Alt = float(input("Sua altura: "))

A = ((BMA + Bme) * Alt) / 2

if BMA and Bme and Alt > 0.0:
    print("A área do trapézio é: ", "%.1f" % A)
elif BMA or Bme < 0.0:
    print("Número Inválido!")
