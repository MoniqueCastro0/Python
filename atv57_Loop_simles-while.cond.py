while True:
    string = input("Digite uma string: ")
    print(f"A string digitada é: {string}")

    tamanho = len(string) #tamanho da string digitada
    print(f"O tamanho dessa string digitada é de: {tamanho} caracteres")
    resultado = 20 - tamanho # tamanho da string digitada menos 20
    

    if tamanho < 20: 
        print("*" * resultado + string)
        break

print("Fim")