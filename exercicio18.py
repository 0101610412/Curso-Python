Op = input("Escolha uma operação matemática (+, -, x ou /): ")

Num1 = float(input("Digite o primeiro número: "))
Num2 = float(input("Digite o segundo número: "))

if Op == '+':
    soma = Num1 + Num2
    print("Soma: ", soma)
elif Op == '-':
    sub = Num1 - Num2
    print("Subtração: ", sub)
elif Op == 'x':
    mult = Num1 * Num2
    print("Multiplicação: ", mult)
elif Op == '/':
    div = Num1 / Num2
    print("Divisão: ", div)
