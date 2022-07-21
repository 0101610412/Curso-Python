SalarioBase = float(input("Entre com o salário-base do funcionário: "))

SalarioComGrat = (SalarioBase * 5) / 100
SalarioComImposto = (SalarioBase * 7) / 100
Receber = (SalarioBase + SalarioComGrat) - SalarioComImposto

print("O funcionário receberá: ", "R$", "%.2f" % Receber)