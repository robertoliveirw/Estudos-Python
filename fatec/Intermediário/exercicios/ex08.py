'''Exercício Resolvido 11.2
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com 3 casas decimais. 
Usar o método . write ()'''

N = float(input('Digite um número real: '))
arq = open('ex_08_ex_resolvido_11.2.txt', 'w')

while N != 0:
    arq.write(f'{N:.3f} \n')
    N = float(input('Digite um número real: '))

arq.close()

print('\n Fim do programa')
