nome = "Stefany"
cidade = "Curitiba"
estado = "Paraná"
cep = 81350268
nomeInput = input("Digite um nome: ")

if nomeInput == nome:
    print(f"Seus dados são: {nome}, {cidade}, {estado}, {cep}")

if nomeInput != nome:
    print("Esse usuário não existe em nossas bases de dados")