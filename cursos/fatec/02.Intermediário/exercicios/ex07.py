'''Exercício Resolvido 11.1
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
Usar o método .write()'''

N = int(input('Digite um número: \n'))
arq = open('ex_07_ex_resolvido_11.1.txt', 'w')

while N != 0:
    arq.write(f'{N} \n')
    N = int(input('Digite um número: '))

arq.close()
print('\n Fim do programa')