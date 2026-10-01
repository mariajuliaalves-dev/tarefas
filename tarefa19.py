texto = input("Digite o texto: ")

quantidade = len(texto)

print("Quantidade de caracteres:", quantidade)

if quantidade > 280:
    cortar = quantidade - 280
    print("Corte", cortar, "caracteres")