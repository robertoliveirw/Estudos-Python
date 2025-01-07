# Criar um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira

import math
number = float(input('Digite um número real: '))

wholenumber = math.trunc(number)
print(f'A parte inteira do numero {number} é {wholenumber}')
