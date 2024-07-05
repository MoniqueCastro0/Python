import random

numero_secreto = random.randint(1,100)

print(numero_secreto)

palpite = 0

while numero_secreto != palpite: #Enquanto for verdadeiro vai execultar
    
    palpite = int(input("Digite um palpite de número: "))

           #20            69
    if palpite > numero_secreto:
        print("É um número menor! ")
    
    if palpite < numero_secreto:
        print("É um número maior! ")




print("Fim")