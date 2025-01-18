# Adicionar UF no dicionário

UF = {}

print('Leitura de dados \n')
while True:
    sigla = input('Digite a Sigla: ')
    if sigla == '':
        break
    elif sigla in UF:
        print(f'A sigla {sigla} já existe no cadastro.')
        continue
    estado = input('Digite o estado: ')
    capital = input('Digite a capital: ')
    pib = float(input('Digite o PIB: '))

    UF[sigla] = ((estado, capital, pib))

print(UF)