A = float(input("Primeiro valor: "))
B = float(input("Segundo valor: "))
C = float(input("Terceiro valor: "))

if (A < B + C) or (B < A + C) or (C < A + B):
    Triangulo = True
    if (A == B) and (A == C):
        print("Triângulo equilátero!")
    elif (A == B) or (A == C) or (B == C):
        print("Triângulo isósceles!")
    elif (A != B) and (A != C):
        print("Triângulo escaleno!")
elif (A > B + C) or (B > A + C) or (C > A + B):

    print("Não são valores válidos!")
