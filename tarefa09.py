preco = float(input("Preço: "))
dinheiro = float(input("Dinheiro: "))

if dinheiro < preco:
    print("Saldo insuficiente, faminto.")
else:
    troco = dinheiro - preco
    print("Troco:", troco)