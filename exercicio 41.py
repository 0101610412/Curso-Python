ValuePerHour = float(input("Qual o valor por hora trabalhada? "))
HT = int(input("Horas trabalhadas: "))

ValorHorasTrabalhadas = ValuePerHour * HT
VS = (ValorHorasTrabalhadas * 10) / 100
VF = ValorHorasTrabalhadas + VS

print("O funcionário deverá receber: ", "R$", "%.2f" % VF)
