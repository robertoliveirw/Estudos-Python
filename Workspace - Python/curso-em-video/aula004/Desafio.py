# Desafio 01

nome = input('Qual o seu nome? ')

print('Olá, ' + nome + '! Prazer em te conhecer!')

# Desafio 02

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('ano= ')

print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano)

# Desafio 03

N1 = float(input('Primeiro Número: '))
N2 = float(input('Segundo Número: '))

S = N1 + N2

print(f'A soma dos dois números é: {S}')

# Desafio 04

a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')
