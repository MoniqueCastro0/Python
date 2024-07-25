while True: #Inicio do loop
    numero = int(input("Digite um número: ")) 
    if numero  == -1:
        break
    while numero > 0:
        print(numero) #Imprmime o numero
        numero -= 1 #Decrementa o número em 1