tempo = int(input("Quanto tempo durou a chamada?(em segundos) "))
valor = 0.12
minutos = tempo // 60
porcentagem = (((tempo%60)*100)/60)/100

preco = (minutos*valor) + (porcentagem*valor)

print("{:.2f}".format(preco))


