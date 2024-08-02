""" num = [1,2,3,5,6]
indice = int(input("Digite um indice a ser mudado: "))
novovalor = int(input("Digite um valor: "))
num.insert(indice, novovalor)
print(num) """

#sorted faz uma copia da lista e a reordena em crecente
#sorted faz uma copia da lista e a reordena em crecente

#incompleta

pessoas = [["", 0], ["", 0], ["", 0], ["", 0]]


""" while True:
    comando = int(input("1 Busca, 2 Adiciona, 3 Sai: "))

    while True:
        if comando == 2:
          nome = input("Digite o nome do contato: ")
          numero = int(input('Digite o número a ser adicionado: '))
          pessoas[0][0] = nome
          pessoas[0][1] = numero
          print(nome)
          print(numero)
          break

    if comando == 3:
      print("Programa Finalizado!")
      break
    

        

print(pessoas) """

def adicionar():
    nome = input("Digite o nome do contato: ")
    numero = int(input('Digite o número a ser adicionado: '))
    pessoas[0][0] = nome
    pessoas[0][1] = numero
    print(nome)
    print(numero)

adicionar()

def buscar():
    nome = input("Digite o nome do contato a ser buscado: ")
    pessoas[0][0] = nome
    pessoas[0][1] = numero
    print(nome)
    print(numero)

buscar()