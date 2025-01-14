# Média de uma lista


lista = [12, 24, 48, 96]
print(len(lista))

soma = 0

# Estou adicionando a variavel numero para cada item(numero) presente na lista
for numero in lista:
    soma += numero  # Eu preciso somar o número individualmente

media = soma / len(lista)
print("A média dos números é:", media)
