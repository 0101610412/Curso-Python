ValorProd = float(input("Insira o valor do produto: "))

Desc = (ValorProd * 10) / 100
TotPag = ValorProd - Desc
Parc = ValorProd / 3

ParcSN = (input("O produto será parcelado (em 3x)? (s/n): "))

if ParcSN == 's':
    ValorParc = Parc
    ComVenP = (ValorProd * 5) / 100
    print("Total a pagar: ", "%.2f" % ValorProd)
    print("Valor da parcela (em 3x): ", "%.2f" % ValorParc)
    print("Comissão do vendedor: ", ComVenP)
elif ParcSN == 'n':
    ComVen = (TotPag * 5) / 100
    print("Valor a pagar: ", "%.2f" % TotPag)
    print("Comissão do vendedor: ", "%.2f" % ComVen)
