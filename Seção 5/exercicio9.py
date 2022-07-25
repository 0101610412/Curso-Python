SalT = float(input("Informe o valor do salário: "))
ValEmp = float(input("Informe o valor desejado para o empréstimo: "))

ApEmp = (SalT * 20) / 100

if ValEmp > ApEmp:
    print("Empréstimo não concedido!")
else:
    print("Empréstimo concedido!")