distancia = float(input("Distância em km: "))
tempo = float(input("Tempo em minutos: "))

velocidade = distancia / (tempo / 60)

print("Velocidade:", velocidade, "km/h")

if velocidade > 40:
    print("Modo turbo ativado.")