alt = float(input("Insira sua altura: "))
peso = float(input("Insira o seu peso (em kg): "))

if (alt < 1.20) and (peso > 1) and (peso < 60):
    print("Categoria: A")
elif (alt < 1.20) and (peso > 60)and (peso <= 90):
    print("Categoria: D")
elif (alt < 1.20) and (peso > 90):
    print("Categoria: G")
elif (alt < 1.70) and (alt > 1.20) and (peso > 1) and (peso < 60):
    print("Categoria: B")
elif (alt < 1.70) and (alt > 1.20) and (peso > 60) and (peso <= 90):
    print("Categoria: E")
elif (alt < 1.70) and (alt > 1.20) and (peso > 90):
    print("Categoria: H")
elif (alt > 1.70) and (peso > 1) and (peso < 60):
    print("Categoria: C")
elif (alt > 1.70) and (peso > 60) and (peso <= 90):
    print("Categoria: F")
elif (alt > 1.70) and (peso > 90):
    print("Categoria: I")