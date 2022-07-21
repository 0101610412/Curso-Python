import math

print("Sendo a e b os catetos de um triângulo digite seus valores para obter a hipotenusa:")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

hip = math.sqrt(a**2 + b**2)

print("Hipotenusa: ", "%.2f" % hip)
