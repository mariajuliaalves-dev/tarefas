tempo = int(input("Tempo da viagem: "))
musica = float(input("Duração da música: "))

quantidade = int(tempo / musica)

print("Cabem", quantidade, "músicas completas")