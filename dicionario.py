#usado para armazenar dados no formato chave:valor
#são ordenados 
#multaveis 
#não permite elementos duplicados 
#não precisa contem apenas strings

meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["banaani"] = "banana"
meu_dicionario["cembalo"] = "cravo"
print(meu_dicionario)
print(meu_dicionario["apina"])
print("---------------------")
palavra = input("por favor, digite uma palavra: ")

if palavra in meu_dicionario:
    print("Tradução: ", meu_dicionario[palavra])
else:
    print('Palavra não encontrada')