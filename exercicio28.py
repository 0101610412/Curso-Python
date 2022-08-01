import math
print("Entre com 3 números inteiros positivos:")

x = int(input("Primeiro número: "))
y = int(input("Segundo número: "))
z = int(input("Terceiro número: "))

Op = input("Você quer efetuar qual tipo de média?\n A) Geométrica\n B) Ponderada\n "
           "C) Harmônica\n D) Aritmética\n Opção: ")

if Op == 'A':
    geo = math.sqrt(x * y * z)
    print("Geométrica: ", "%.2f" % geo)
elif Op == 'B':
    pond = (x + 2 * y + 3 * z) / 6
    print("Ponderada: ", "%.2f" % pond)
elif Op == 'C':
    harm = 1 / (1 / x + 1 / y + 1 / z)
    print("Harmônica: ", "%.2f" % harm)
elif Op == 'D':
    arit = (x + y + z) / 3
    print("Aritmética: ", "%.2f" % arit)
