'''Enunciado 
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha. Usar o método .write()'''

lista = []

arquivo = open('arquivo_ex_write_lines.txt', 'w')

X = float(input('Digite um número:'))

while X != 0:
    lista.append(f'{X:.3f}\n')
    X = float(input('Digite um número:'))

arquivo.writelines(lista)
arquivo.close()

print('\n Fim do programa')