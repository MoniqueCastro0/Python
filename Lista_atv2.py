#feito
numeros = [18,22,44,13,35,27,16]

def range(lista: list):
    ordenada = sorted(lista)#ordena a lista em tamanho crecente
    menor = ordenada[0]
    maior = ordenada[6]
    diferenca = maior - menor

    print(ordenada)
    print(menor)
    print(maior)
    print(f"A diferença entre o maior e o menor número é de: {diferenca}")

range(numeros)