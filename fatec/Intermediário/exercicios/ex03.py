# Escreva um programa que leia um inteiro Qtde e crie um conjunto com elementos numéricos inteiros aleatórios dentro do intervalo fechado [1, 50]. Mostre o conjunto gerado na tela. Lembre-se que os conjuntos não podem ter elementos repetidos, então a geração de números aleatórios pode representar um problema. Como resolver isso?
# Cuidado: Este programa tem potencial para entrar em laço infinito caso o valor fornecido para Qtde seja maior que 50. 

from random import randint

qtde = int(input('Qual a quantidade de elementos a ser criada entre de 1 até 50?'))
conjunto = set()

if len(conjunto) <= 50:
    while len(conjunto) < qtde:
        conjunto.add(randint(1,50))

    print(f'O Conjunto tem 1 elemento. Sendo ele: {conjunto}') if len(conjunto) == 1 else print(f'O Conjunto tem {len(conjunto)} elementos. Sendo eles: {conjunto} ')
else: 
    print('Número Inválido. Digite algo no intervalo de 1 até 50')