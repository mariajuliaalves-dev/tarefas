fatias = int(input("Fatias: "))
amigos = int(input("Amigos: "))

cada = fatias // amigos
sobrou = fatias % amigos

print(cada, "fatias para cada")
print("Sobraram", sobrou)

if sobrou > 0:
    print("Sobrou pelo menos uma fatia!")