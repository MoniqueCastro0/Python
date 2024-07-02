tentativas = 0
seupin = int(input("Digite um PIN: "))

while True:
    codigo = int(input("Digite seu PIN: ")) #entrada
    tentativas += 1 #incrementa mais 1
    if codigo == seupin:
        sucesso = True #se verdadeiro a var sucesso recebe verdadeiro
        break

    if tentativas == 3:
        sucesso = False
        break
    print("Incorreto....Tente novamente")

if sucesso:
    print("PIN correto inserido!")
else:
    print("Muitas tentativas...")


#do Prof
#tentativas = 0

#while True:
    #codigo = input("Digite seu PIN: ") #entrada
    #tentativas += 1
    #if codigo == "1234":
      #  sucesso = True #se verdadeiro a var sucesso recebe verdadeiro
     #   break

    #if tentativas == 3:
   #     sucesso = False
  #      break
 #   print("Incorreto....Tente novamente")

#if sucesso:
 #   print("PIN correto inserido!")
#else:
    #print("Muitas tentativas...")