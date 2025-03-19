# Projeto de Advinhação de palavras similar ao termo / wordly
import random

palavras = ['Brasil', 'Argentina', 'Uruguai', 'Chile']

palavra_sorteada = random.choice(palavras).lower()
palavra_escondida = '-' * len(palavra_sorteada)

letras_escolhidas = []

max_tentativas = 10
tentativas = 0

print('Palavra Atual: ' , palavra_escondida, '\n') 

while True:
    tentativas += 1
    chute = input('Digite uma Letra: ').lower()

    if chute in letras_escolhidas:
        print(f'Você já escolheu a letra {chute}')
        continue
    
    letras_escolhidas.append(chute)
   
    if chute in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if chute == palavra_sorteada[indice]:
                lista.append(chute)
            else: 
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista)
        print(palavra_escondida)
    else:
        max_tentativas -= 1
        print(f'Letra {chute} não encontrada. Você tem mais {max_tentativas} tentativas. \n Tente novamente. \n')
    
    if palavra_escondida == palavra_sorteada:
        print(f'Parabéms! \n Você acertou a palavra sorteada: {palavra_sorteada} em {tentativas} tentativas.')
        break
    elif max_tentativas == 0:
        print('Você atingiu o limite máximo de tentativas. \n Fim de jogo. ')
        break