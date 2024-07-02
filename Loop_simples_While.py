#O bloco de codigo dentro do laço while sera execultado equando a condição for verdadeira
#Quando se torna falsa para de execultar

while True:
    numero = int(input("Digite um número: ")) #se tirar daqui fica em um laço infinito

    if numero == -1:
        break

    print(numero ** 2)


print("Programa encerrado, obrigado! ")