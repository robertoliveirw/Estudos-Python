# Pensar (entre 0 e 5) em um número e dizer se o usuário acertou ou não

import random
numeroaleatorio = random.randint(0, 5)
numero = int(input('Em qual número de 0 a 5 eu estou pensando? '))

if numeroaleatorio == numero:
    print('Você acertou!')
else:
    print(f'Você errou, estou pensando no número {numeroaleatorio}')
