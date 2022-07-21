K = float(input("Digite quantos KM/h (quilômetros por hora) serão convertidos para m/s (metros por segundo): "))

M = K/3.6

"""
Tipos de formatações para escolher o numero de casas decimais 
"""

# print("KM/h para m/s: ", round(M, 5))

print("KM/h para m/s: ", "%.5f" % M)