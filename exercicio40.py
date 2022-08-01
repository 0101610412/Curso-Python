CF = float(input("Insira o custo de fábrica: "))

if (CF > 0) and (CF <= 12000):
    PercentualDistribuidor = ((CF * 5) / 100) + CF
    print("Custo ao consumidor: ", "%.2f" % PercentualDistribuidor)
elif (CF > 12000) and (CF <= 25000):
    PercentualDistribuidor = (CF * 10) / 100
    PercentualImpostos = (CF * 15) / 100
    CustoConsumidor = PercentualDistribuidor + PercentualImpostos + CF
    print("Custo ao consumidor: ", "%.2f" % CustoConsumidor)
elif CF > 25000:
    PercentualDistribuidor = (CF * 15) / 100
    PercentualImpostos = (CF * 20) / 100
    CustoConsumidor = PercentualDistribuidor + PercentualImpostos + CF
    print("Custo ao consumidor: ", "%.2f" % CustoConsumidor)