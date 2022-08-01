print("Para saber se você pode ou não aposentar preencha os seguintes dados:")
Id = int(input("Digite quantos anos você têm: "))
TempSer = int(input("Tempo de serviço: "))

if (Id >= 65) or (TempSer >= 30):
    print("Aprovado!")
elif (Id >= 60) and (TempSer >= 25):
    print("Aprovado!")
else:
    print("Você não tem os requisitos para se aposentar!\n \n")
    print("REQUISITOS PARA APOSENTADORIA:\n"
          "·Ter pelo menos 65 anos;\n"
          "·Ou ter trabalhado pelo menos 30 anos;\n"
          "·Ou ter pelo menos 60 anos de idade e 25 anos de trabalho.")