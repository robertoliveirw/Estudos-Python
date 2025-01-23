# Exemplo 12.10
'''Empacotamento de dados com tupla'''

# Função Criada
def somatorio (*dados): # O * Indica que é uma tupla
    r = 0 
    for i in dados:
        r += i
    return r

# Código principal
v = somatorio(1,2,3,4,5)
print(v)