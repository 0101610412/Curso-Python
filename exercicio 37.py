val = float(input("Insira o valor do produto: "))

desc = (val * 12) / 100
VCD = val - desc

print("Valor do produto com 12% de desconto: ", "%.2f" % VCD)