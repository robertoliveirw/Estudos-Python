lista = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in lista:
        lista.append(n)
        print('Valor inserido.')

    else: 
        print('Valor já cadastrado.')

    print(lista)

    c = str(input('Deseja continuar? [S/N]')).upper()   
    
    if c == 'N':
        print(f'\nA sua lista em ordem crescente: {sorted(lista)}')
        print(f'A sua lista em ordem decrescente: {sorted(lista, reverse=True)}')
        break

    else: 
        print('Certo, pode adicionar mais números.')
        continue
