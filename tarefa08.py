tamanho = float(input("Tamanho do arquivo: "))
velocidade = float(input("Velocidade da internet: "))

tempo = tamanho * 8 / velocidade

print("Download em", tempo, "segundos")