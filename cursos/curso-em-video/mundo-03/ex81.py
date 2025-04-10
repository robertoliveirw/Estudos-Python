lista = []

while True:
    n = int(input('Digite um Número: '))

    lista.append(n)

    c = str(input('Deseja continuar? [S/N]')).upper()
    if c == 'S':
        continue
    else:
        print(f'Você digitou {len(lista)} elementos.')
        print(f'Os valores em ordem descrescente são {sorted(lista, reverse=True)}')
        if 5 in lista:
            print('o Valor 5 faz parte da Lista.')
            break
        else:
            print('O valor 5 não faz parte da lista.')
            break