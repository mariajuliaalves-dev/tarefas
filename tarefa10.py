bateria = float(input("Bateria: "))
consumo = float(input("Consumo por hora: "))

horas = bateria / consumo

print("Vai durar", horas, "horas")

if bateria < 20:
    print("Corre pra tomada!")