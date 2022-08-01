print("Informe sua data de aniversário com dia, mês e ano")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if (dia > 0) and (dia <= 28) or (dia <= 29):
    mes = 2
elif (dia > 0) and (dia <= 30):
    mes = 4, 6,  9, 11
elif (dia > 0) and (dia <= 31):
    mes = 1, 2, 3, 5, 7, 8, 10, 12
elif (mes > 0) and (mes < 13):
    mes = ano
elif ano <= 2008:
    print("Data Válida!")
    