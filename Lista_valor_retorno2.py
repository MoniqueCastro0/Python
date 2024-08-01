#Retorna uma lista
def entrada_numeros():
    numeros = []
    while True:
        entrada_usuario = input("Digite um número inteiro, deixe em branco para sair: ")
        if len(entrada_usuario) == 0:
            break
        numeros.append(int(entrada_usuario))
    return numeros