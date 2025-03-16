# Jogo da Forca
import random

# Solicitar as palavras ao usuário
palavras = []

while True:
    adicionar_palavra = input('Digite a palavra que você deseja adicionar ao jogo. \n Caso queira finalizar encerrar, digite 0. \n Palavra a ser adicionada:')
    if adicionar_palavra == '0':
        break
    else: 
        palavras.append(adicionar_palavra)
    

# Sorteia uma palavra dentro da lista
palavra_sorteada = random.choice(palavras) 
# 'Esconde' a palavra
palavra_escondida = '-' * len(palavra_sorteada)

letras_escolhidas = []

max_tentativas = 10
tentativas = 0 

# Lógica

while True:
    tentativas += 1
    letra = input('Digite uma Letra:  \n').lower()

    if letra in letras_escolhidas:
        print(f'Você já escolheu a letra {letra}.' )
        continue

    letras_escolhidas.append(letra)

    if letra in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else: 
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista)
        print(palavra_escondida)

    else:
        max_tentativas -= 1
        print(f'Letra {letra} não encontrada. Você tem mais {max_tentativas} tentativas. \n Tente novamente. \n')

    if palavra_escondida == palavra_sorteada:
        print(f'Parabéms! \n Você acertou a palavra sorteada: {palavra_sorteada} em {tentativas} tentativas.')
        break
    elif max_tentativas == 0:
        print('Você atingiu o limite máximo de tentativas. \n Fim de jogo. ')
        break
