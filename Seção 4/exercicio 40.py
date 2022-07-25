DT = int(input("Quantos dias o encanador trabalhará? "))

VD = DT * 30
VDCI = (VD * 8) / 100
VF = VD - VDCI

print("Quantia líquida que deverá ser paga ao encanador: ", "%.2f" % VF)