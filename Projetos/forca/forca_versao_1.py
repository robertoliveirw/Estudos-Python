# Jogo da Forca
import random

palavras = ['brasil', 'argentina', 'canada', 'mexico', 'franca', 'alemanha', 'italia', 'japao', 'china', 'india', 'australia', 'russia', 'espanha', 'egito', 'suecia']

palavra_sorteada = random.choice(palavras) # Sorteia uma palavra dentro da lista
palavra_escondida = '-' * len(palavra_sorteada) # 'Esconde' a palavra

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

# Após finalizar o código colocar uma opção para o usuário escrever as suas palavras