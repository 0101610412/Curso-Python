print("CALCULADOR DE CONSUMO")
km = float(input("Insira a distância em km: "))
L = float(input("Quantos litros foram abastecidos? "))

consumo = km / L

if consumo < 8:
    print("Venda o carro!")
elif (consumo > 8) and (consumo < 14):
    print("Econômico!")
elif consumo > 12:
    print("Super econômico!")
