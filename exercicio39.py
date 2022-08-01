salAtual = float(input("Valor do salário atual do trabalhador: "))
tempServ = int(input("Tempo de serviço do funcionário na empresa: "))

if (salAtual > 0) and (salAtual <= 500):
    if tempServ < 1:
        reaj = ((salAtual * 25) / 100) + salAtual
        print("Salário com reajuste (sem bônus: ", "%.2f" % reaj)
elif (salAtual > 0) and (salAtual <= 1000):
    if (tempServ >= 1) and (tempServ <= 3):
        reaj = ((salAtual * 20) / 100) + 100 + salAtual
        print("Salário com reajuste e bônus de R$100.00: ", "%.2f" % reaj)
elif (salAtual > 0) and (salAtual <= 1500):
    if (tempServ >= 4) and (tempServ <= 6):
        reaj = ((salAtual * 15) / 100) + 200 + salAtual
        print("Salário com reajuste e bônus de R$200.00: ", "%.2f" % reaj)
elif (salAtual > 0) and (salAtual <= 2000):
    if (tempServ >= 7) and (tempServ <= 10):
        reaj = ((salAtual * 10) / 100) + 300 + salAtual
        print("Salário com reajuste e bônus de R$300.00: ", "%.2f" % reaj)
elif (salAtual > 2000) and (tempServ > 10):
    salario = salAtual + 500
    print("Salário sem reajuste pelo valor do salário atual e tempo de serviço (bônus R$500.00: ", "%.2f" % salario)
    