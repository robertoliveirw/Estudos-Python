# Exemplo 12.10
'''Empacotamento de dados com tupla'''

# Função Criada
def MontaSaida (*dados, sep=', '):
    saida = sep.join(dados)
    return saida

# Código principal
itens = MontaSaida('Maçã', 'Laranja', 'Banana', 'Melão')
print(itens)
