'''Ler vários números inteiros. Mostrar a média, o menor e o maior, e perguntar se o usuário quer continuar ou não'''
lista = []
controlador = 0

while controlador != 5: 
    controlador = int(input('''
    ----- Qual Operação deseja realizar? -----
    [1] Adicionar Número
    [2] Menor número
    [3] Maior número
    [4] Média
    [5] sair
    ------------------------------------------
    '''))
    if controlador == 1:
        n = int(input('Digite um número para adicionar a lista [Digite 0 para parar de adicionar números]: '))
        lista.append(n)
        while n != 0:
            n = int(input('Digite um número para adicionar a lista [Digite 0 para parar de adicionar números]: '))
            lista.append(n)
            print(lista)
    elif controlador == 2:
        mi = min(lista)
        print(f'O menor valor na lista é {mi}')
    elif controlador == 3:
        ma = max(lista)
        print(f'O maior valor na lista é {ma}')
    elif controlador == 4:
        med = sum(lista)/len(lista)
        print(f'A média da lista é {med}')

print('Muito obrigado, programa finalizado!')
