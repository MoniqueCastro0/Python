#incomleto

notas = []
qtdnotas = int(input("Digite a quantidade de notas a qual vai ser enserido: "))

while qtdnotas != qtdnotas:
    n = int(input("Digite a nota: "))
    notas.append(n)

def media(notas):
    media = sum(notas) / len(notas) #sum soma todos os valores da lista
    print(f"A media das notas é: {media}")

media(notas)