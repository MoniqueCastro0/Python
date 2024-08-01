#incom

lista = []

while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    em_ordem = sorted(lista)
    print(em_ordem)

    if numero == 0:
        break
    
    
    