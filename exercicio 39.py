print("A importância de R$780.000,00 será repartida entre 3 ganhadores, sendo 46% para o primeiro, 32% para o segundo"
      " e o restante para o terceiro")

pr1 = (780.000 * 46) / 100
pr2 = (780.000 * 32) / 100
pr3 = 780.000 - pr1 - pr2

print("Prêmio do primeiro ganhador: ", "%.3f" % pr1)
print("Prêmio do segundo ganhador: ", "%.3f" % pr2)
print("Prêmio do terceiro ganhador: ", "%.3f" % pr3)
