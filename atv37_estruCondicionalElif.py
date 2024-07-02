#incompleta
ano = int(input("Digite um ano: "))

if ano / 4:
    print("Esse ano é bissexto")

elif ano / 100 and ano / 400:
    print("Tambem é um número bissexto")

else:
    print("Não é um ano bissexto")