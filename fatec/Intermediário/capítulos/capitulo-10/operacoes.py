# Dicionário completo com todas as UFs e a quantidade
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
    'SC': 'Santa Catarina',
    'QTDE': '27'
}

# Exemplos de operações

# 1. .clear() - Remove todos os elementos do dicionário
UF_clear = UF.copy()
UF_clear.clear()
print("Dicionário após clear():", UF_clear)

# 2. .copy() - Cria uma cópia do dicionário
UF_copy = UF.copy()
print("\nCópia do dicionário:", UF_copy)

# 3. .fromkeys() - Cria um dicionário com chaves e valores padrão
chaves = ['PA', 'MA', 'TO']
novo_dict = dict.fromkeys(chaves, 'Região Norte')
print("\nNovo dicionário com .fromkeys():", novo_dict)

# 4. .get() - Obtém o valor de uma chave com segurança
estado = UF.get('MA')
print("\nEstado encontrado com .get():", estado)
estado_inexistente = UF.get('XX', 'Não encontrado')
print("Estado inexistente com .get():", estado_inexistente)

# 5. .items() - Retorna os itens como pares de tuplas
itens = UF.items()
print("\nItens do dicionário com .items():", list(itens))

# 6. .keys() - Retorna todas as chaves do dicionário
chaves = UF.keys()
print("\nChaves do dicionário com .keys():", list(chaves))

# 7. .pop() - Remove um item e retorna o valor associado
valor_removido = UF.pop('QTDE')
print("\nValor removido com .pop():", valor_removido)
print("Dicionário após .pop():", UF)

# 8. .popitem() - Remove e retorna o último par chave-valor inserido
ultimo_item = UF.popitem()
print("\nÚltimo item removido com .popitem():", ultimo_item)
print("Dicionário após .popitem():", UF)

# 9. .setdefault() - Adiciona uma chave com valor padrão se não existir
valor_default = UF.setdefault('PA', 'Pará Default')
print("\nValor retornado com .setdefault():", valor_default)
print("Dicionário após .setdefault():", UF)

# 10. .update() - Atualiza o dicionário com outro dicionário
atualizacoes = {'MA': 'Maranhão Atualizado', 'PI': 'Piauí Atualizado'}
UF.update(atualizacoes)
print("\nDicionário após .update():", UF)

# 11. .values() - Retorna todos os valores do dicionário
valores = UF.values()
print("\nValores do dicionário com .values():", list(valores))
