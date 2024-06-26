#Media de notas - 3

#nota1 = float(input("Digite a 1° nota: "))
#nota2 = float(input("Digite a 2° nota: "))
#nota3 = float(input("Digite a 3° nota: "))

#media = (nota1 + nota2 + nota3) / 3

#print(f"A sua média é de: {round(media,2)}")


#vereficando se n é par ou impar - 4

#numero = int(input("Digite um número: "))

#if numero % 2 == 0:
    #print("Número é Par")

#else:
    #print("Número é Impar")

#Maior n de uma lista;

#lista = [3, 7, 8, 6, 10, 2] #lista = []  - lista.append(3)
#print(max(lista))

#for i in lista: #percorre cada posição e mostra os números
    #print(i)


#Calculo Salario
salario = float(input("Digite o valor bruto do salario: "))
horasExtras = float(input("Digite o valor a ser pago de horas extrs: "))
descontos = float(input("Digite o valor de descontos: "))
remuneracao = float(input("Digite o vvalor de rumeneração: "))
valorPagar = (salario + horasExtras + remuneracao) - descontos 

print(f"O valor a ser pago a esse fúncionario é de: {valorPagar}")
