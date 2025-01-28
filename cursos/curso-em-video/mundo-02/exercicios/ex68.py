'''Jogar par ou ímpar. Só será interrompido quando o jogador perder, mostrando a quantidade de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint


contador = 0

while True:
    # Contagem
    contador += 1
    # Par ou Ímpar (Computador)
    variavel_pc = randint(1,2)    
    
    # Par ou Impar (Usuário)
    variavel_usuario = input('Você desejar Par ou Ímpar? [P/I]').strip().upper()
    
    # Str para Int - Do Usuário
    if variavel_usuario == 'P':
        variavel_usuario = 2
        print(variavel_usuario)
    elif variavel_usuario == 'I':
        variavel_usuario = 1
        print(variavel_usuario)
    else:
        print('Entrada Inválida!')

    soma = variavel_pc + variavel_usuario

    if soma % 2 == 0:
        print('Você ganhou!')
    else:
        print('Você Perdeu!')
        print(f'Foram necessárias {contador} tentativas para a máquina te vencer!')
        break