#incom

adiOUremo = int(input("Digite 1 para adicionar e 2 para remover: "))
numero = int(input("Digite o número a ser adicionado: "))
lista = []


while True:
    if adiOUremo == 1:
        lista.append(numero)
        print(lista)
        break

    while True:
        print("É necessario adicionar pelo menos um valor a lista para continuar: ")


        lista.pop(0)
        print(lista)
        brea