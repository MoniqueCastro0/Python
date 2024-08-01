#Semelhante a arry arranjo
#Armazena mutiplos elementos em uma unica var
minha_lista = []
minha_lista2 = [1,2,3,4]
print(minha_lista2[0])
print(f"A soma dos dois primeiros indices é {minha_lista2[0] + minha_lista2[1]}") #somando o indice 1 mais o indece 2
#acessando indice(começa em 0 ) da lista

#Adicionar intens na lsita  
numeros = []
numeros.append(5)# append adiciona no fim da lista
numeros.append(10)
numeros.append(3)
print(numeros)


#Adicionar intens em um lugar espercifico da lsita 
num = [1,2,3,5,6]
num.insert(3, 10) #o 1° numero é indice da onde deve ser adicionado
print(num)

#remover itens
lista_remover = [1, 2, 3, 4, 5, 6]
lista_remover.pop(2)
print(lista_remover)
lista_remover.remove(2) #Remove algum
print(lista_remover)

#sort ordenação da propria lista
min_lista = [2,5,1,2,4]
min_lista.sort()
print(min_lista)

#sorted faz uma copia da lista e a reordena em crecente
original = [2,5,1,2,4]
em_ordem = sorted(original)
print(original)
print(em_ordem)