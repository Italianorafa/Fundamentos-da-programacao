segundos = int(input("Insira um horário em segundos: "))
horas = segundos//3600
resto = segundos%3600
minutos = resto//60
segundos = resto%60
print("{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
