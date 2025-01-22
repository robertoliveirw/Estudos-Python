'''Exercício Resolvido 11.3
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com 3 casas decimais. 
Usar o método . writelines ()'''

lst = []
N = float(input('Digite um número real: '))
arq = open('ex_09_ex_resolvido_11.3.txt', 'w')

while N != 0:
    lst.append(f'{N:.3f} \n')
    N = float(input('Digite um número real: '))

arq.writelines(lst)
arq.close()
print('\n Fim do programa')
