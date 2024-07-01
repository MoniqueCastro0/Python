idade = int(input("Digite sua idade: "))

if idade < 5 and idade > 0:
    print("Suspeito que você ainda não saiba escrever")

elif idade <= 0 or idade > 150:
    print("Isso deve ser um erro")

else:
    print(f"Ok, você tem {idade} anos.")