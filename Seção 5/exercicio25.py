import math

print("Escreva abaixo uma equação para obter sua raíz:")

ax = float(input("ax²: "))
bx = float(input("bx: "))
c = float(input("c: "))

if ax == 0:
    print("Não é uma equação de 2º grau!")
elif ax != 0:
    X = ax**2 + bx + c

x1 = -bx + math.sqrt(bx**2 - 4 * ax * c) / 2 * ax
x2 = -bx - math.sqrt(bx**2 - 4 * ax * c) / 2 * ax

if x1 < 0:
    print("Não existe raíz!")
elif x1 == 0:
    print("Raíz única:\n", x1)
elif x1 > 0:
    print("x1: ", x1)
    print("x2: ", x2)

