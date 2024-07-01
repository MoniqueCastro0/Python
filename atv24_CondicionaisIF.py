previsao = int(input("Qual é a previsão do tempo para amanhã? Temeratura: "))
vaiChover = input("Vai chover (Sim/Não): ")

if previsao >= 20:
    print("Use jeans e camiseta")


if previsao < 20 and previsao >= 10:
    print("Use jeans e camiseta, Recomendo um suéter também.")

if previsao < 10 and previsao > 0:
    print("Use um casaco, calça e botas!!!")

if previsao < 0 and previsao < 5:
    print("Muito frio se agasalhe muito bem!!!")

if vaiChover == "Sim":
    print("Leve um guarda-chuvas")