'''Exercício Resolvido 11.4
Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor
Usar um laço while e na leitura usar o método .readline()'''

lst = []
arq_ent = open('ex_10_ex_resolvido_11.4.txt', 'r') # Abrir o arquivo para leitura
linha = arq_ent.readline()  # Lê a primeira linha do arquivo

while linha != '':
    lst.append(int(linha))
    linha = arq_ent.readline() # Pula p/ a próxima linha do arquivo

arq_ent.close()

print('Valores Lidos')
print(lst)

s = sum(lst)
q = len(lst)
m = s / q
mi = min(lst)
ma = max(lst)

print(f'Soma: {s}')
print(f'Quantidade: {q}')
print(f'Quantidade: {q}')
print(f'Média: {m}')
print(f'Valor mínimo: {mi}')
print(f'Valor máximo: {ma}')
print('\n Fim do programa')