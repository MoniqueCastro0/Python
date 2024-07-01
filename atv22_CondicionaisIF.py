#in
salarioHora = int(input("Digite o salário por hora: "))
horasTra = int(input("Digite as horas trabalhadas: "))
dia = input("Digite dia da semana: ")

if dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta" or dia == "sexta" or dia == "sabado":
    print(f"Salario diário = {salarioHora * horasTra}")

if dia == "domingo":
    print(f"Salario diário = {salarioHora * 2}")

