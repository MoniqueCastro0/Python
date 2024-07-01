#Converter temperatura graus Fahrennheit para graus celsius e imprimir uma mensagem
temperatura = float(input("Digite uma temperatura em graus Fahrenheit: "))

grausCelsios = (temperatura - 32) * (5 / 9)
print(f"Essa temperatura em graus celsius é: {grausCelsios}")

if grausCelsios < 0:
    print("Brr! Está frio aqui!")
