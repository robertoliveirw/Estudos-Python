# Exemplo 12.21
'''Função  filter -  função filter em Python é usada para filtrar elementos de um iterável (como uma lista, tupla ou conjunto) com base em uma função que retorna True ou False. Apenas os elementos que satisfazem a condição (isto é, onde a função retorna True) serão incluídos no resultado.. '''

numeros = [1, 2, 3, 4, 5, 6]

# Usando filter para selecionar apenas números pares
pares = filter(lambda x: x % 2 == 0, numeros)

print(list(pares))  # Saída: [2, 4, 6]
