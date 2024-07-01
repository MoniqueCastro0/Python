preco = float(input("Digite o valor do produto: "))

if preco <= 50:
    print("Categoria Econômica")

if preco > 50 and preco <= 100:
    print("Categoria Intermediária")

else:
    print("Categoria Premium")