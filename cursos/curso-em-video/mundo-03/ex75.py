'''
Desenvolva um programa que leias quatro valores e guarde-os em uma tupla. No final mostre:
A - Quantas vezes apareceu o número 9
B - Em que posição foi digitado no primeiro valor 3 
C - Quais números são pares
'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: ')) 
n4 = int(input('Digite o quarto valor: '))

contador_9 = 0
contador_3 = 0

tupla_numeros = (n1, n2, n3, n4)

# A
for i in tupla_numeros:
    if i == 9:
        contador_9 += 1
if contador_9 > 0:
    print(f'O número 9 aparece {contador_9} vezes.') 
else:
    print('O número 9 não aparece')

# B
for x in tupla_numeros:
    if '3' in str(x): 
        contador_3 = x

if contador_3 > 0:
    print(f'O número 3 apareceu pela primeira vez na posição {contador_3}')
else: 
    print('O número 3 não aparece')

# C
for y in tupla_numeros:
    if y % 2 == 0:
        print(f'O número {y} é par.')
   # else: 
   #    print(f'O número {y} é ímpar. ')