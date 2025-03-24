'''
Crie um programa que gere 5 numeros aleatórios e colocar numa tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

n1, n2, n3, n4, n5 = randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)
tupla_numeros = (n1, n2, n3, n4, n5)
val_max = max(tupla_numeros)
val_min = min(tupla_numeros)
print(f'Números gerados: {tupla_numeros}. \n O valor mínimo é: {val_min}. \n O valor máximo é: {val_max}.')

