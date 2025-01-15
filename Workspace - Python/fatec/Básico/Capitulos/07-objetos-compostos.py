# Ler vários números e adicionar a uma lista


numeros = []


while True:

    entrada = input(
        'Digite um número para adicionar a lista ou digite \'FIM\' para finalizar.').strip()

    if entrada.upper() == 'FIM':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print('Comando Inválido. Digite \'FIM\' para finalizar ou ou digite um número.')

print('A lista de números é:', numeros)
