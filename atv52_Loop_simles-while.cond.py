import random

numero_secreto = random.randint(1,100)

print(numero_secreto)

tentativas = 0

while numero_secreto == palpite:
    palpite = int(input("Digite um palpite de número: "))

    if numero_secreto < palpite:
        print("É um número maior! ")
    else:
        print("É um número menor! ")

print("Fim")