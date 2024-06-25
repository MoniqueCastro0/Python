precoProduto = float(input("Digite o valor do prouto:"))
percentualDesconto = int(input("Digite o percentual de desconto:"))

desconto = (percentualDesconto / 100) * precoProduto

print(f"o seu valor de desconto é de: {precoProduto - desconto}")


#imc = peso / (altura / 100) ** 2
#{(percentualDesconto / 100) * precoProduto}