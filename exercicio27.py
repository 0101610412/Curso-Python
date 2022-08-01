idade = int(input("Digite a idade do(a) nadador(a) para saber sua categoria: "))

if (idade <= 7) or (idade == 5):
    print("Categoria: Infantil A")
elif (idade <= 10) or (idade == 8):
    print("Categoria: Infantil B")
elif (idade <= 13) or (idade == 11):
    print("Categoria: Juvenil A")
elif (idade <= 17) or (idade == 14):
    print("Categoria: Juvenil B")
elif idade > 18:
    print("Categoria: Sênior")
