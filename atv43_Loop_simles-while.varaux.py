#Escreva um programa que pergunte ao usuário um ano e imprima o próximo ano bissexto.
ano = int(input("Digite aqui o ano"))

if(ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print("É ano bisexto")

else:
    print("Não é Bisexto")