#incompleta
# ano = int(input("Digite um ano: "))

# if ano / 4:
#     print("Esse ano é bissexto")

# elif ano / 100 and ano / 400:
#     print("Tambem é um número bissexto")

# else:
#     print("Não é um ano bissexto")


ano = int(input("Digite aqui o ano"))

if(ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print("É ano bisexto")

else:
    print("Não é Bisexto")