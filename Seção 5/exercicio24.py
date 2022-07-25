ValorProd = float(input("Qual é o valor do produto? "))
Est = input("Para qual estado o produto será destinado (MG/SP/RJ/MS)? ")

ImpMG = (ValorProd * 7) / 100
ImpSP = (ValorProd * 12) / 100
ImpRJ = (ValorProd * 15) / 100
ImpMS = (ValorProd * 8) / 100

if Est == 'MG':
    TotPag = ValorProd + ImpMG
    print("Total a pagar acrescido de 7% de imposto: ", "%.2f" % TotPag)
elif Est == 'SP':
    TotPag = ValorProd + ImpSP
    print("Total a pagar acrescido de 12% de imposto: ", "%.2f" % TotPag)
elif Est == 'RJ':
    TotPag = ValorProd + ImpRJ
    print("Total a pagar acrescido de 15% de imposto: ", "%.2f" % TotPag)
elif Est == 'MS':
    TotPag = ValorProd + ImpMS
    print("Total a pagar acrescido de 8% de imposto: ", "%.2f" % TotPag)
else:
    print("ERRO! POR FAVOR, INSIRA UM ESTADO VÁLIDO!")
