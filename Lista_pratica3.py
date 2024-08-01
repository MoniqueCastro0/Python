#Apenas adiciona e Remove

lista = []


while True:
    adiOUremo = int(input("Digite 1 para adicionar e 2 para remover: "))
    if len(lista) == 0: #para saber se tem algo na lsita
        print("É necessario adicionar pelo menos um valor a lista para continuar: ")
        numero = int(input("Digite o número a ser adicionado: "))


    if adiOUremo == 1: #Adicionar
        numero = int(input("Digite o número a ser adicionado: "))
        lista.append(numero)
        print(lista)

    if adiOUremo == 2: #Remover
        numero = int(input("Digite o número a ser removido: "))
        print(lista)
        lista.remove(numero)
        print(lista)

    
        

    """ while True:
        print("É necessario adicionar pelo menos um valor a lista para continuar: ")
        lista.pop(0)
        print(lista)
        break """