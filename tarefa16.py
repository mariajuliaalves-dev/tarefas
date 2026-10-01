horas = float(input("Horas de impressão: "))
preco = float(input("Preço do kWh: "))

consumo = horas * 0.35
custo = consumo * preco

print("Custo da impressão: R$", custo)