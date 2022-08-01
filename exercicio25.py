import math

print("Escreva abaixo os coeficientes de uma equação de 2º grau para obter sua raíz:")

ax = float(input("ax²: "))
bx = float(input("bx: "))
c = float(input("c: "))

if ax < 0:
    print("Não é equação do 2º grau!")

delta = bx**2 - 4 * ax * c

if delta < 0:
    print("Não existe raíz!")
elif delta == 0:
    x = -bx / (2*ax)
    print("Raíz única: ", x)
elif delta > 0:
    x1 = (-bx + math.sqrt(delta)) / (2 * ax)
    x2 = (-bx - math.sqrt(delta)) / (2 * ax)
    print("Temos como solução duas raízes diferentes")
    print("x1: ", "%.2f" % x1)
    print("x2: ", "%.2f" % x2)
