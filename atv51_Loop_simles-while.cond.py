#incom

import re

tentativas = 0



while True:
    codigo = input("Digite seu PIN: ") 
    tamanho = len(codigo)
    tentativas += 1

    if tamanho == 8:
        sucesso = True 
        break


    
    
    print("Incorreto....Tente novamente")
    


if sucesso:
    print("PIN correto inserido!")
    print(f"Você tentou inserir o codigo: {tentativas} vezes")
else:
    print("Muitas tentativas...")