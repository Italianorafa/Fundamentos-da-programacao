moradores= int(input("Quantos moradores? "))
andares = int(input("Quantos andares? "))
PA = ((1 + andares)/2) * andares

viagens = moradores * 4
viagens_ano = viagens * 365

dist = (3*viagens_ano*PA)
total_km = dist/1000
horas = dist/3600
print("O elevador viajou {:.2f}Km e funcionou por {:.2f} horas.".format(total_km, horas))
