lista   = []
lista_par =[]
lista_impar = []

while True:
    n = int(input('Digite um Número: '))

    lista.append(n)

    c = str(input('Deseja continuar? [S/N]')).upper()
    if c == 'S':
        continue
    else:
        for i in lista:
            if i % 2 == 0:
                lista_par.append(i)
            else:
                lista_impar.append(i)
    
    print('-='*30)
    print(f'A Lista completa é: {lista}')
    print('-='*30)
    print(f'Lista de números pares: {lista_par}')
    print('-='*30)
    print(f'Lista de números ímpares: {lista_impar}')
    break