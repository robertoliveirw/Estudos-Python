# import math
# Eu posso usar o from math import sqrt (ou qualquer outra funcionalidade) para importar uma funcionalidade específica.
# number = int(input('Digite um número: \n'))
# squareroot = math.sqrt(number)

# print(f'A raiz quadrada de {number} é igual a {squareroot:.2f}')

from math import sqrt

number = float(input('Digite um número: \n'))
squareroot = sqrt(number)

print(f'A raíz quadrada de {number} é igual a {squareroot:.2f}')
