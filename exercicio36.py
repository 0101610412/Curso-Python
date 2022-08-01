valMen = float(input("Insira o valor mensal de venda para obter o valor da comissão: "))

if valMen >= 100000:
    cms = ((valMen * 16) / 100) + 700
    print("Comissão: ", "%.2f" % cms)
elif (valMen < 100000) and (valMen >= 80000):
    cms = ((valMen * 14) / 100) + 650
    print("Comissão: ", "%.2f" % cms)
elif (valMen < 80000) and (valMen >= 60000):
    cms = ((valMen * 14) / 100) + 600
    print("Comissão: ", "%.2f" % cms)
elif (valMen < 60000) and (valMen >= 40000):
    cms = ((valMen * 14) / 100) + 550
elif (valMen < 40000) and (valMen >= 20000):
    cms = ((valMen * 14) / 100) + 500
    print("Comissão: ", "%.2f" % cms)
elif valMen < 20.000:
    cms = ((valMen * 14) / 100) + 400
