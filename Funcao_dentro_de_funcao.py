def cumprimentar(nome):
    print("Olá", nome)

def cumprimentar_varias_vezes(nome, vezes):
    while vezes > 0:
        cumprimentar(nome)
        vezes -= 1

cumprimentar_varias_vezes("Monique", 3)