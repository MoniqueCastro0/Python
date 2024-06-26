#Juros Simples

capital = float(input("Digite o capital ínicial:"))
taxa = float(input("Digite o valor da taxa de Juros anual: "))
Tempo = float(input("Digite o tempo em anos: "))
juros = capital * (taxa / 100) * Tempo # taxa / 100 - para jogar para numero em porcentagem

print(f"O valor Total em Juros é de: {juros}")

- teste