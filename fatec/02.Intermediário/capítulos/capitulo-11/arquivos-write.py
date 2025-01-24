'''Enunciado 
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha. Usar o método .write()'''

arquivo = open('saida_er_11.1.txt', 'w') #O w é para indicar que será utilizado para gravação

num = int(input('Digite um número. Caso o número for igual a 0 o programa será encerrado.'))
while num != 0:
    arquivo.write(f'{num}\n') # É necessário gravar como string, por isso está sendo utilizando o f{}
    num = int(input('Digite um número. Caso o número for igual a 0 o programa será encerrado.'))
arquivo.close()

print('\n Fim do Programa')