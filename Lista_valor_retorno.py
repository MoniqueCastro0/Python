#Recebe uma lista como parametro

show_tamanhos = [45, 44, 36, 39, 40]
def mediana(minha_lista: list):
    ordenada = sorted(minha_lista)#sorted faz uma copia da lista e a reordena em crecente
    centro_lista = len(ordenada) // 2
    return ordenada[centro_lista]

print("A mediana é", mediana(show_tamanhos))

idade = [1, 56, 34, 22, 5, 77, 5]
print("A mediana das idades é", mediana(idade))