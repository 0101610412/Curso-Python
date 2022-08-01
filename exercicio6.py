print("A seguir digite dois números inteiros e descubra qual o maior e a diferença entre eles")

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    print("O maior número é: ", num1)
else:
    print("O maior número é: ", num2)

dif = num1 - num2
print("A diferença entre eles é: ", dif)
