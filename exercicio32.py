print("CARDÁPIO:\n Cachorro Quente (R$1.20 un) - cód: 100\n Bauru Simples (R$1.30 un) - cód: 101")
print(" Bauru com Ovo (R$1.50 un) - cód: 102\n Hamburguer (R$1.20 un) - cód: 103")
print(" Cheeseburguer (R$1.70 un) - cód: 104\n Suco (R$2.20 un) - cód: 105")
CodLan = int(input(" Refrigerante (R$1.00 un) - cód: 106\n DIGITE O CÓDIGO DO QUE IRÁ PEDIR: "))

cachorro_quente = 1.20
bauru_simples = 1.30
bauru_com_ovo = 1.50
hamburguer = 1.20
cheeseburguer = 1.70
suco = 2.20
refrigerante = 1.00

quant = int(input("Quantas unidades? "))

if CodLan == 100:
    val = cachorro_quente * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
elif CodLan == 101:
    val = bauru_simples * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
elif CodLan == 102:
    val = bauru_com_ovo * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
elif CodLan == 103:
    val = hamburguer * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
elif CodLan == 104:
    val = cheeseburguer * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
elif CodLan == 105:
    val = suco * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
elif CodLan == 106:
    val = refrigerante * quant
    print("TOTAL A PAGAR: ", "%.2f" % val)
