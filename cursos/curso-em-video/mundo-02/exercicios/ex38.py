'''Ler dois números inteiros e dizer qual o maior'''

n1 =  int(input('Digite um número: '))
n2 =  int(input('Digite um número: '))

if n1 > n2:
    print(f'{n1} é maior do que {n2}')
elif n2 > n1:
    print(f'{n2} é maior do que {n1}')
else: 
    print('Os números são iguais')