#feito

def linha(inteiro, texto):
    linhaTexto = texto[0] * inteiro

    contador = 0
    while contador < inteiro:
        contador += 1
        print(linhaTexto)

        if texto == " ":
            print(inteiro * "*")

linha(5, "Monique")
