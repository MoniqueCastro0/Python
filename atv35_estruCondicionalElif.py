pontos = int(input("Digite a quantidade de pontos: "))

if pontos < 0:
    print("impossível!")

elif pontos >= 0 and pontos <= 49:
    print("falhar")

elif pontos >= 50 and pontos <= 59:
    print("1")

elif pontos >= 60 and pontos <= 69:
    print("2")

elif pontos >= 70 and pontos <= 79:
    print("3")

elif pontos >= 80 and pontos <= 89:
    print("4")

elif pontos >= 90 and pontos <= 100:
    print("5")

else:
    print("impossível!")