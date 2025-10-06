print ("Vamos calcular tua nota!")
CTP = float(input("Insira a nota na componente teórico-prática: "))
CP = float(input("Insira a nota da componente prática:"))

if CTP >= 6.5 and CP >= 6.5:
    NF = (0.3 * CTP) + (0.7 * CP)
else:
    NF = 66

if NF < 10:
    print("\nReprovado em época normal.\nVamos calcular com as notas do recurso!\n")
    ATPR = float(input("Insira a nota na componente de recurso teórico-prática:"))
    APR = float(input("Insira a nota da componente de recurso prática:"))
    if ATPR >= 6.5 and APR >= 6.5:
        NF = (0.3 * max(CTP,ATPR)) + (0.7 * max(CP,APR))

if NF == 66:
    print("Reprovado por nota mínima!")
else:
    print("Sua nota final foi {:.2f}".format(NF))
