''' Escreva um programa que leia do teclado dados dos Estados Brasileiros. Siglam, nome, capital e pib. A sigla deve ser usada como chave para o dicionário e o valor deve ser uma tupla formada com nome capital e pib. Finalizar o código quando uma sitring vazia der entrada.'''

UF = {}

print('Início do Programa')

while True:
    sigla = input('Digite a sigla do estado: ')
    if sigla == '':
        print(f'\n Fim do programa.')
        break
    elif sigla in UF:
        print(f'\n A sigla:  {sigla} já existe no programa.')
        continue 
    estado = input('Digite o nome do estado: ')
    capital = input('Digite a capital do estado: ')
    pib = float(input('Digite o pib do estado: '))
    UF[sigla] = ((estado, capital, pib))

print(f'A lista é essa: {UF}')   