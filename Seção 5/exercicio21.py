print("Escolha a opção:\n 1 - Soma de 2 números.\n 2 - Diferença entre 2 números (maior pelo menor).\n"
      "3 - Produto entre 2 números.\n 4 - Divisão entre 2 números (o denominador não pode ser 0)." )

Opc = int(input("Opção: "))
Num1 = float(input("Primeiro número: "))
Num2 = float(input("Segundo número: "))

if Opc == 1:
    soma = Num1 + Num2
    print("Soma: ", soma)
elif Opc == 2:
    sub = Num1 - Num2
    print("Diferença: ", sub)
elif Opc == 3:
    mult = Num1 * Num2
    print("Produto: ", mult)
elif Opc == 4:
    div = Num1 / Num2
    print("Divisão: ", div)
