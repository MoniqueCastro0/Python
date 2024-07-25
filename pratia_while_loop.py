#feito
string1 = input("Por favor, digite uma string: ")
string2 = input("Por favor, digite outra string: ")

if len(string1) > len(string2):
    print(f"A maior string é {string1}")
else:
    print(f"A maior string é {string2}")


if len(string1) == len(string2):
    print("As string são iguais")

