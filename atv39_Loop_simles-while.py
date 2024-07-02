from math import sqrt

while True:
    numeros = int(input("Digite alguns números inteiros: "))

    if numeros <= 0:
        print("Número inválido")
        break

    else:
        print(sqrt(numeros))