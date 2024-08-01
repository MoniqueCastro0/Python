#feito
while True:
    lista = [1,2,3,4,5]
    indice = int(input("Digite um indice a ser mudado: "))
    novovalor = int(input("Digite um valor: "))
    lista.insert(indice, novovalor)
    print(lista)
    
    if indice == -1:
        break
