#incompleta

pessoas = [["", 0]]


while True:
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
    

        

print(pessoas)



