'''Aprimorar desafio 28 (numero entre 0 e 10), mas dessa vez pedindo até a pessoa acertar, e no final mostre quantas tentativas foram necessárias'''
import random

numeroaleatorio = random.randint(0, 10)
numero = int(input('Em qual número de 0 a 10 eu estou pensando? '))
cont = 1

while numeroaleatorio != numero: 
    if numeroaleatorio != numero:
        print(f'Você errou, tente novamente!')
        numero = int(input('Em qual número de 0 a 10 eu estou pensando? '))
        cont += 1
        
print('Você acertou!')
print(f'Foram necessárias {cont} tentativas até acertar!')

