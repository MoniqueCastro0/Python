nome1 = input("Digite o seu nome: ")
idade1 = int(input("Digite a sua idade: "))

nome2 = input("Digite seu nome: ")
idade2 = int(input("Digite sua idade: "))

if idade1 > idade2 and idade1 >= 65:
    print(f"{nome1} é o idoso: ")

elif idade2 > idade1 and idade2 >= 65:
    print(f"{nome2} é o idoso: ")

else:
    print("Ninguem é idoso")