import math

num = float(input("Insira um número para obter seu quadrado e sua raíz quadrada, caso seja positivo: "))

if num > 0:
    print("Número elevado ao quadrado: ", num**2)
    print("Raíz Quadrada: ", "%.2f" % math.sqrt(num))