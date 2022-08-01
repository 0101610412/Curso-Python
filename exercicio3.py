import math

num = float(input("Insira um número para obter sua raíz quadrada: "))

if num > 0:
    print("Sua raíz quadrada é: ", "%.2f" % math.sqrt(num))
else:
    print(num**2)
    