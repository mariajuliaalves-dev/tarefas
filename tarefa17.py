valor = float(input("Valor da compra: "))

if valor > 100:
    desconto = valor * 15 / 100
    valor_final = valor - desconto

    print("Valor final:", valor_final)
    print("Você economizou:", desconto)
else:
    print("Valor final:", valor)