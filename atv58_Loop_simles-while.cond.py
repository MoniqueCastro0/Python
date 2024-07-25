string = input("Digite uma string: ")

tamanho = len(string) #tamanho da string digitada
resultado = (30 - tamanho) / 2 
print(round(resultado))
      
                       #4      13
nova_string = "*" * round(resultado) + string + "*" * round(resultado)

if len(nova_string) % 2 != 0:
    nova_string += "*"

print("*" * 30)
print(nova_string)
print("*" * 30)