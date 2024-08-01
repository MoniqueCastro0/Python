lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
]

def contagens(minnha_lista):
    palavras = {} #iniciando um dicionario
    for palavra in minnha_lista:
        #se a palavra ainda não está no dicionario, inicialize o valor com zero

        if palavra not in palavras: #se palavra não estiver dentro do dicinario palvras

                      #chave    #valor
            palavras[palavra] = 0 #acessando a chave

        #incrementa o valor 
        palavras[palavra] += 1
        return palavras
    
#chama a função
print(contagens(lista_palavras))
