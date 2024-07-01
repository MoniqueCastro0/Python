gol_casa = int(input("Pontuação de casa: "))
gol_fora = int(input("Pontuação de fora: "))

if gol_casa > gol_fora:
    print("O Time de casa é campeão: ")

elif gol_fora > gol_casa:
    print("O Time de fora é campeão: ")

else:
    print("Empate!")