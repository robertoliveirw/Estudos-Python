# Iteção - Falar os itens do dicionário atraves de uma tupla 

UF = {
    'AC': 'Acre',
    'AM': 'Amazonas',
    'AP': 'Amapá',
    'PA': 'Pará',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'TO': 'Tocantins',
    'AL': 'Alagoas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'MA': 'Maranhão',
    'PB': 'Paraíba',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RN': 'Rio Grande do Norte',
    'SE': 'Sergipe',
    'DF': 'Distrito Federal',
    'GO': 'Goiás',
    'MS': 'Mato Grosso do Sul',
    'MT': 'Mato Grosso',
    'ES': 'Espírito Santo',
    'MG': 'Minas Gerais',
    'RJ': 'Rio de Janeiro',
    'SP': 'São Paulo',
    'PR': 'Paraná',
    'RS': 'Rio Grande do Sul',
    'SC': 'Santa Catarina'
}

print('Início do Programa \n O dicionário é esse:')
contador = 1

for SIGLA, ESTADO in UF.items():
    print(f'{contador} -- {SIGLA} - {ESTADO}')
    contador += 1

print('\n Fim do programa')