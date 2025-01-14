# Média de uma lista

lista = []

print('Início do programa!')

while True:

    entrada = input(
        'Digite um número para adicioná-lo a lista ou digite \'Sair\' para finalizar.').strip()
    if entrada.upper() == 'SAIR':
        break

    try:
        numero = float(entrada)
        lista.append(numero)

    except ValueError:
        print('Comando Inválido. Digite \'Sair\' para finalizar ou ou digite um número.')

media = sum(lista) / len(lista)

print("A média dos números é:", media)
