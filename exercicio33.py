PA = float(input("Informe o preço antigo: "))

ValAtual1 = PA - ((PA * 5) / 100)
ValAtual2 = PA - (PA * 10) / 100
ValAtual3 = PA - (PA * 15) / 100

if (PA > 1) and (PA < 50):
    print(ValAtual1)
elif (PA > 50) and (PA < 100):
    print(ValAtual2)
elif PA > 100:
    print(ValAtual3)

if (ValAtual1 > 1) and (ValAtual1 < 50) or (ValAtual2 > 1) and (ValAtual2 < 50) or (ValAtual3 > 1) and (ValAtual3 < 50):
    print("Barato")
elif (ValAtual1 > 80) and (ValAtual1 <= 120) or (ValAtual2 > 80) and (ValAtual2 <= 120) or (ValAtual3 > 80) and (ValAtual3 <= 120):
    print("Normal")
elif (ValAtual1 > 120) and (ValAtual1 <= 200) or (ValAtual2 > 120) and (ValAtual2 <= 200) or (ValAtual3 > 120) and (ValAtual3 <= 200):
    print("Caro")
elif (ValAtual1 > 200) or (ValAtual2 > 200) or (ValAtual3 > 200):
    print("Muito caro")
