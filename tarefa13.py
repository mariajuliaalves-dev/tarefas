peso = float(input("Peso do aluno: "))
mochila = float(input("Peso da mochila: "))

porcentagem = mochila / peso * 100

print("A mochila representa", porcentagem, "% do seu peso")

if porcentagem > 10:
    print("Mochila pesada demais!")