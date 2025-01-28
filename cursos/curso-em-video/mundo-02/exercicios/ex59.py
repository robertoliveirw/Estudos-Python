'''Ler dois valores e mostrar um menu com as opções [1]Somar[2]Multiplicar[3]maior(qual o maior)[4]novos numeros[5]sair do programa'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
cont = 0

while cont != 5:
    cont = int(input('''
    ----- Qual Operação deseja realizar? -----
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] novos números
    [5] sair
    ------------------------------------------
    '''))
    if cont == 1:
        s = n1 + n2
        print(f'A soma é igual a: {s}')
    elif cont == 2:
        m = n1 * n2
        print(f'A soma é igual a: {m}')
    elif cont == 3:
        if n1 > n2:
            print(f'n1 = {n1} é maior que n2 = {n2}.')
        else:
            print(f'n2 = {n1} é maior que n1 = {n2}.')
    elif cont == 4:
        print('Informe os numeros novamente:')      
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: ')) 
    elif cont == 5:
        print('Programa finalizado!')
    else:
        print('Código Inválido')
