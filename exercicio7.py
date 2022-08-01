print("Insira dois números e descubra qual o maior: ")

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if num1 > num2:
    print("O maior número é: ", "%.2f" % num1)
elif num1 == num2:
    print("Os números são iguais!")
else:
    print("O maior número é: ", "%.2f" % num2)
