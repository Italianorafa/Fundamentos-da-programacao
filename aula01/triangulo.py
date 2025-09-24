import math

adj = float(input("Insira o valor do cateto adjacente: "))
ops = float(input("Insira o valor do cateto oposto: "))
hip = math.hypot(adj,ops)
angle_rad = math.acos((adj/hip))
angle_deg = math.degrees(angle_rad)
print("Hipotenusa = {:.2f}, ângulo = {:.2f}".format(hip, angle_deg))
