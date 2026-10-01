limite = float(input("Limite da via: "))
velocidade = float(input("Velocidade do carro: "))

if velocidade > limite:
    excesso = velocidade - limite
    print("Excesso de", excesso, "km/h")
    print("Multa de R$ 130,16")
else:
    print("Boa viagem, motorista!")